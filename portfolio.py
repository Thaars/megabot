from definitions import STOP_LOSS_LEVEL, COMMISSION, STARTING_AMOUNT
import math


class Portfolio:
    def __init__(self, df, starting_amount, *args, **kwargs):
        self.orders = list()
        self.cash = starting_amount
        self.points = 0
        self.winning = {
            0: 0,
            1: 0
        }
        self.losing = {
            0: 0,
            1: 0
        }
        self.market_start_amount = 0
        self.market_end_amount = 0
        self.df = df

    def undo_all_open(self):
        # this is done by undoing the last openings
        for order in self.orders:
            commission = round(order['buying_price'] * order['units'] * COMMISSION, 2)
            self.cash += order['units'] * order['buying_price'] + commission

    def create_order(
            self,
            df,
            index,
            current_price,
            target=None,
            stop_loss=None,
            target_2=None,
            stop_loss_2=None,
            trade_type='long'
    ):
        # only buy, when enough cash is available

        rounding = len(str(current_price)) - 2
        units = round_down(self.cash / current_price, rounding)
        commission = round(current_price * units * COMMISSION, 2)

        if units > 0 and self.cash > 1:
            # only buy, when unit per share is buyable for remaining cash
            if units * current_price < self.cash:
                # print(f"ID:{len(self.orders)}, CREATE {units} units at {current_price}")
                self.cash -= units * current_price + commission
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
                #                   stop_loss_2=stop_loss_2 if stop_loss_2 is not None else stop_loss,
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
        close_price = None
        for order in self.orders:
            # bullish
            if order['trade_type'] == 'long':
                if row[stop_loss_long_limit_key] <= order['stop_loss']:
                    self.close_order(order, order['stop_loss'], index)
                    close_price = order['stop_loss']
                elif row[target_long_limit_key] >= order['target']:
                    self.close_order(order, order['target'], index)
                    close_price = order['target']
            # bearish
            if order['trade_type'] == 'short':
                if row[stop_loss_short_limit_key] >= order['stop_loss']:
                    self.close_order(order, order['stop_loss'], index)
                    close_price = order['stop_loss']
                elif row[target_short_limit_key] <= order['target']:
                    self.close_order(order, order['target'], index)
                    close_price = order['target']
            return True
        return False

    def close_order(self, order, price, index):
        # bullish
        if order['trade_type'] == 'long':
            if price > order['buying_price']:
                self.winning[order['order_id']] += 1
            else:
                self.losing[order['order_id']] += 1
            self.cash += order['units'] * price
            self.points += price - order['buying_price']
        # bearish
        if order['trade_type'] == 'short':
            diff = order['units'] * order['buying_price'] - order['units'] * price
            if price < order['buying_price']:
                self.winning[order['order_id']] += 1
            else:
                self.losing[order['order_id']] += 1
            self.cash += (order['units'] * order['buying_price']) + diff
            self.points += order['buying_price'] - price
        # all
        commission = round(order['buying_price'] * order['units'] * COMMISSION, 2)
        self.cash -= commission
        self.orders = [o for o in self.orders if o != order]
        self.df.loc[index, 'close_order'] = price

    # def close_order2(self, df, index, order_id, price):
    #     order = [x for x in self.orders if order_id == x.get('order_id')]
    #     if not order:
    #         return
    #     order = order[0]
    #
    #     self.cash += order['units'] * price
    #     comission = round(order['buying_price'] * order['units'] * COMMISSION, 2)
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
