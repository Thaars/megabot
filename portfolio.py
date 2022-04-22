import datetime

from definitions import *
import math


class Portfolio:
    def __init__(self, df, starting_amount, *args, **kwargs):
        self.orders = list()
        self.cash = starting_amount
        self.tick_cash = 0
        self.lowest_tick_cash = 0
        self.ticks = 0
        self.winning_ticks = 0
        self.losing_ticks = 0
        self.winning = {
            0: 0,
            1: 0
        }
        self.winners = list()
        self.losers = list()
        self.loser_series = {
            'total_cash': 0,
            'series': list()
        }
        self.largest_loser_series = {
            'total_cash': 0,
            'series': list()
        }
        self.losing = {
            0: 0,
            1: 0
        }
        self.market_start_amount = 0
        self.market_end_amount = 0
        self.max_stop_loss_amount = 0
        self.df = df

    def undo_all_open(self):
        # this is done by undoing the last openings
        for order in self.orders:
            commission_factor = round(order['buying_price'] * order['units'] * COMMISSION_FACTOR, 2)
            commission_value = round(COMMISSION_VALUE, 2)
            self.cash += order['units'] * order['buying_price'] + commission_factor
            self.tick_cash += commission_value

    def is_currently_a_trading_break(self, current_time):
        if USE_TRADING_BREAKS:
            for trading_break in TRADING_BREAKS:
                break_from_time = datetime.datetime.strptime(trading_break['from'], '%H:%M').time()
                break_to_time = datetime.datetime.strptime(trading_break['to'], '%H:%M').time()
                if break_from_time < current_time < break_to_time:
                    return True
        return False

    def create_order(
            self,
            df,
            index,
            current_price,
            target=None,
            stop_loss=None,
            target_2=None,
            trade_type='long',
    ):
        # check fro trading breaks
        if self.is_currently_a_trading_break(current_time=index.time()):
            return False

        # trade only buy, when enough cash is available
        rounding = len(str(current_price)) - 2
        units = round_down(self.cash / current_price, rounding)
        commission_factor = round(current_price * units * COMMISSION_FACTOR, 2)
        commission_value = round(COMMISSION_VALUE, 2)

        # at this point we have a special target rule
        # it's a string separated by `:`
        if str(target).__contains__(':'):
            target_type, target_when, target_key = target.split(':')
            if target_type == 'candle' and target_when == 'next':
                target = {
                    'when': index + datetime.timedelta(minutes=TIMEFRAME_MINUTE_MAPPING[TIMEFRAME]),
                    'key': target_key
                }

        if units > 0 and self.cash > 1:
            # only buy, when unit per share is buyable for remaining cash
            if units * current_price < self.cash:
                # print(f"ID:{len(self.orders)}, CREATE {units} units at {current_price}")
                self.cash -= units * current_price + commission_factor
                self.tick_cash -= commission_value
                order1 = dict(order_id=len(self.orders),
                              buying_price=current_price,
                              units=units,
                              target=target,
                              stop_loss=stop_loss,
                              trade_type=trade_type)
                # if target_2 is not None:
                #     order2 = dict(order_id=len(self.orders) + 1,
                #                   buying_price=current_price,
                #                   units=units / 2,
                #                   target_2=target_2,
                #                   trade_type=trade_type)
                #
                # if target_2:
                #     order1['units'] = units / 2
                #     self.orders.append(order2)

                self.orders.append(order1)

                df.loc[index, 'create_order'] = current_price

                return True
            return False

    def close_position(
        self,
        line,
        index,
        row,
        undo_all_open=False,
        stop_loss_long_limit_key='low',
        target_long_limit_key='high',
        stop_loss_short_limit_key='high',
        target_short_limit_key='low'
    ):
        if undo_all_open:
            # the end of the tested timeframe has arrived
            # undo the last position opening, because closing at any point could distort the result
            self.undo_all_open()
        for order in self.orders:
            # bullish
            if order['trade_type'] == 'long':
                # check for trading breaks
                if self.is_currently_a_trading_break(current_time=index.time()):
                    self.close_order(order, row['close'], index)
                # stop loss
                elif row[stop_loss_long_limit_key] <= order['stop_loss']:
                    self.close_order(order, order['stop_loss'], index)
                    stop_loss_diff = order['buying_price'] - order['stop_loss']
                    if stop_loss_diff > self.max_stop_loss_amount:
                        self.max_stop_loss_amount = stop_loss_diff
                # target simple
                elif not isinstance(order['target'], dict) and row[target_long_limit_key] >= order['target']:
                    self.close_order(order, order['target'], index)
                # target special
                elif isinstance(order['target'], dict):
                    if 'when' in order['target'] and order['target']['when'] == index:
                        self.close_order(order, row[order['target']['key']], index)
            # bearish
            if order['trade_type'] == 'short':
                # check fro trading breaks
                if self.is_currently_a_trading_break(current_time=index.time()):
                    self.close_order(order, row['close'], index)
                # stop loss
                elif row[stop_loss_short_limit_key] >= order['stop_loss']:
                    self.close_order(order, order['stop_loss'], index)
                    stop_loss_diff = order['stop_loss'] - order['buying_price']
                    if stop_loss_diff > self.max_stop_loss_amount:
                        self.max_stop_loss_amount = stop_loss_diff
                # target simple
                elif not isinstance(order['target'], dict) and row[target_short_limit_key] <= order['target']:
                    self.close_order(order, order['target'], index)
                # target special
                elif isinstance(order['target'], dict):
                    if 'when' in order['target'] and order['target']['when'] == index:
                        self.close_order(order, row[order['target']['key']], index)
        if self.loser_series['total_cash'] < self.largest_loser_series['total_cash']:
            # remember as largest
            self.largest_loser_series['total_cash'] = self.loser_series['total_cash']
            self.largest_loser_series['series'] = self.loser_series['series']

    def close_order(self, order, price, index):
        # bullish
        if order['trade_type'] == 'long':
            price_diff = price - order['buying_price']
            # round ticks down
            current_ticks = math.floor(price_diff / TICK_SIZE)
            self.tick_cash += current_ticks * TICK_VALUE
            if self.tick_cash < self.lowest_tick_cash:
                self.lowest_tick_cash = self.tick_cash
            if price > order['buying_price']:
                self.winning[order['order_id']] += 1
                self.winning_ticks += current_ticks
                self.winners.append(round(price_diff, 2))
                # reset loser series
                self.loser_series['total_cash'] = 0
                self.loser_series['series'] = list()
            else:
                self.losing[order['order_id']] += 1
                self.losing_ticks += current_ticks
                self.losers.append(round(price_diff, 2))
                self.loser_series['total_cash'] += price_diff
                self.loser_series['series'].append(round(price_diff, 2))
            self.cash += order['units'] * price
            self.ticks += current_ticks
        # bearish
        if order['trade_type'] == 'short':
            price_diff = order['buying_price'] - price
            # round ticks down
            current_ticks = math.floor(price_diff / TICK_SIZE)
            self.tick_cash += current_ticks * TICK_VALUE
            if self.tick_cash < self.lowest_tick_cash:
                self.lowest_tick_cash = self.tick_cash
            diff = order['units'] * order['buying_price'] - order['units'] * price
            if price < order['buying_price']:
                self.winning[order['order_id']] += 1
                self.winning_ticks += current_ticks
                self.winners.append(round(price_diff, 2))
                # reset loser series
                self.loser_series['total_cash'] = 0
                self.loser_series['series'] = list()
            else:
                self.losing[order['order_id']] += 1
                self.losing_ticks += current_ticks
                self.losers.append(round(price_diff, 2))
                self.loser_series['total_cash'] += price_diff
                self.loser_series['series'].append(round(price_diff, 2))
            self.cash += (order['units'] * order['buying_price']) + diff
            self.ticks += current_ticks
        # all
        commission_factor = round(order['buying_price'] * order['units'] * COMMISSION_FACTOR, 2)
        commission_value = round(COMMISSION_VALUE, 2)
        self.cash -= commission_factor
        self.tick_cash -= commission_value
        self.orders = [o for o in self.orders if o != order]
        self.df.loc[index, 'close_order'] = price

    # def close_order2(self, df, index, order_id, price):
    #     order = [x for x in self.orders if order_id == x.get('order_id')]
    #     if not order:
    #         return
    #     order = order[0]
    #
    #     self.cash += order['units'] * price
    #     comission = round(order['buying_price'] * order['units'] * COMMISSION_FACTOR, 2)
    #     self.cash -= comission
    #
    #     self.orders = [x for x in self.orders if order_id != x.get('order_id')]
    #     df.loc[index, 'close_order'] = price

    # def adjust_stop_price_for_orders(self, df, index, stop_loss=None):
    #     # Todo refactor
    #     sl = STOP_LOSS_LEVEL
    #     for order in self.orders:
    #         if order['stop_loss']:
    #             # new_stop_price = df.loc[index, 'Close'] /100 * (sl)
    #             if order['stop_loss'] >= df.loc[index, 'Low']:
    #                 # close order
    #                 self.negative += 1
    #                 self.close_order(df, index, order['order_id'], order['stop_loss'])
    #                 # Marker for Plot
    #                 df.loc[index, 'close_order'] = order['stop_loss']
    #             # elif new_stop_price > order['stop_loss']:
    #             #     # increase stop price, if the new stop price is higher, then till now
    #             #     order['stop_loss'] = new_stop_price
    #
    #         if order.get('limit') and order['limit'] <= df.loc[index, 'High']:
    #
    #             self.positive1 += 1
    #             self.close_order(df, index, order['order_id'], order['limit'])
    #             # Marker for Plot
    #             df.loc[index, 'close_order_l'] = order['limit']
    #             # adjust SL for second limit
    #             if len(self.orders) > 0:
    #                 self.orders[0]['stop_loss'] = self.orders[0]['buying_price']
    #             order2 = list(filter(lambda x: x['order_id'] == order.get('order_id') + 1, self.orders))
    #
    #         if order.get('limit2') and order['limit2'] <= df.loc[index, 'High']:
    #             self.positive2 += 1
    #             self.close_order(df, index, order['order_id'], order['limit2'])
    #             # Marker for Plot
    #             df.loc[index, 'close_order_l2'] = order['limit2']

    # def check_stop_loss_and_limit(self, df, index):
    #     for order in self.orders:
    #         if order['stop_loss'] and order['stop_loss'] >= df.loc[index, 'Low']:
    #             # close order
    #             self.close_order(df, index, order['order_id'], order['stop_loss'])
    #             # Marker for Plot
    #             print("STOP LOSS")
    #             df.loc[index, 'close_order'] = order['stop_loss']
    #         if order['limit'] and order['limit'] <= df.loc[index, 'High']:
    #             self.close_order(df, index, order['order_id'], order['limit'])
    #             # Marker for Plot
    #             df.loc[index, 'close_order'] = order['limit']

    # def current_gains(self, current_price):
    #     gains = self.cash
    #
    #     for order in self.orders:
    #         gains += order['units'] * current_price
    #
    #     return gains

    # def close_all_orders(self, df, price, index=None):
    #     for order in self.orders:
    #         self.close_order(df, index or df.index[-1], order['order_id'], price)

    def get_performance(self):
        result = float(round(((self.cash * 100) / STARTING_AMOUNT) - 100, 2))
        return result

    def get_market_performance(self):
        return float(round(((self.market_end_amount * 100) / self.market_start_amount) - 100, 2))


def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier
