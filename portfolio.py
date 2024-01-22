import datetime

import definitions
from definitions import *
import math


class Portfolio:
    def __init__(self, df, starting_amount, *args, **kwargs):
        self.orders = list()
        self.cash = starting_amount
        self.market_start_amount = 0
        self.market_end_amount = 0
        self.max_stop_loss_amount = 0
        self.df = df
        self.cycles_for_stats = list()
        self.order_count = 0

    def undo_all_open(self):
        # this is done by undoing the last openings
        for order in self.orders:
            commission_factor = round(order['buying_price'] * order['units'] * COMMISSION_FACTOR, 2)
            self.cash += order['units'] * order['buying_price'] + commission_factor
        self.orders = list()

    def create_order(
            self,
            df,
            index,
            current_price,
            target=None,
            stop_loss=None,
            units=None
    ):
        # trade only buy, when enough cash is available
        rounding = len(str(current_price)) - 2
        if units is None:
            units = round_down(self.cash / current_price, rounding)
        commission_factor = round(current_price * units * COMMISSION_FACTOR, 2)

        if units > 0 and self.cash > 1:
            # only buy, when unit per share is buyable for remaining cash
            if units * current_price < self.cash:
                self.cash -= units * current_price + commission_factor
                order = dict(order_id=len(self.orders),
                              buying_price=current_price,
                              units=units,
                              target=target,
                              stop_loss=stop_loss,
                              index=index)

                self.orders.append(order)
                self.order_count += 1

                df.loc[index, 'create_order'] = current_price

                return order
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
            # # stop loss
            # elif stop_loss_long_limit_key is not None and row[stop_loss_long_limit_key] <= order['stop_loss']:
            #     self.close_order(order, order['stop_loss'], index)
            #     stop_loss_diff = order['buying_price'] - order['stop_loss']
            #     if stop_loss_diff > self.max_stop_loss_amount:
            #         self.max_stop_loss_amount = stop_loss_diff
            # # target simple
            # elif target_long_limit_key is not None and not isinstance(order['target'], dict) \
            # and row[target_long_limit_key] >= order['target']:
            #     self.close_order(order, order['target'], index)
            # # target special
            # elif isinstance(order['target'], dict):
            #     if 'when' in order['target'] and order['target']['when'] == index:
            #         self.close_order(order, row[order['target']['key']], index)
            # else:
            self.close_order(order, row['close'], index)

    def close_order(self, order, price, index):
        self.cash += order['units'] * price
        commission_factor = round(order['buying_price'] * order['units'] * COMMISSION_FACTOR, 2)
        self.cash -= commission_factor
        self.orders = [o for o in self.orders if o != order]
        self.df.loc[index, 'close_order'] = price

    def get_first_order(self):
        if len(self.orders) > 0:
            return self.orders[0]
        return None

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

    def get_performance(self, total_cash=None):
        if total_cash is not None:
            return float(round(((total_cash * 100) / STARTING_AMOUNT) - 100, 2))
        return float(round(((self.cash * 100) / STARTING_AMOUNT) - 100, 2))

    def get_market_performance(self):
        return float(round(((self.market_end_amount * 100) / self.market_start_amount) - 100, 2))


def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier
