from definitions import STOP_LOSS_LEVEL, COMMISSION
import math

class Portfolio:
    def __init__(self, starting_amount, *args, **kwargs):
        self.orders = list()
        self.cash = starting_amount
        self.positive = 0
        self.negative = 0

    def create_order(self, df, index, instrument, current_price, limit=None, lower_stop=None):
        # only buy, when enough cash is available

        rounding = len(str(current_price)) - 2
        units = round_down(self.cash / current_price, rounding)
        comission = round(current_price * units * COMMISSION, 2)

        if units > 0 and self.cash > 1:
            # only buy, when unit per share is buyable for remaining cash
            if units * current_price < self.cash:
                #print(f"ID:{len(self.orders)}, CREATE {units} units at {current_price}")
                self.cash -= units * current_price + comission
                self.orders.append(dict(id=len(self.orders),
                                        buying_price=current_price,
                                        instrument=instrument,
                                        units=units,
                                        limit=limit,
                                        lower_stop=lower_stop))
                df.loc[index, 'create_order'] = current_price

                return True
            return False



    def close_order(self, df, index, id, price):
        order = [x for x in self.orders if id == x.get('id')]
        if not order:
            return
        order = order[0]

        if order['instrument'] == 'long':
            self.cash += order['units'] * price
            comission = round(order['buying_price'] * order['units'] * COMMISSION, 2)
            # self.cash -= comission

        if order['instrument'] == 'short':
            profit_percentage = abs((order['buying_price'] / price))
            # print(profit_percentage, order['buying_price'], price)
            self.cash += order['units'] * order['buying_price'] * profit_percentage

        self.orders = [x for x in self.orders if id != x.get('id')]
        df.loc[index, 'close_order'] = price

    def adjust_stop_price_for_orders(self, df, index, stop_loss=None):
        # Todo refactor
        sl = STOP_LOSS_LEVEL
        for order in self.orders:
            if order['lower_stop']:
                # new_stop_price = df.loc[index, 'Close'] /100 * (sl)
                if order['lower_stop'] >= df.loc[index, 'Low']:
                    # close order
                    self.negative += 1
                    self.close_order(df, index, order['id'], order['lower_stop'])
                    # Marker for Plot
                    df.loc[index, 'close_order'] = order['lower_stop']
                # elif new_stop_price > order['lower_stop']:
                #     # increase stop price, if the new stop price is higher, then till now
                #     order['lower_stop'] = new_stop_price

            if order['limit'] and order['limit'] <= df.loc[index, 'High']:
                self.positive += 1
                self.close_order(df, index, order['id'], order['limit'])
                # Marker for Plot
                df.loc[index, 'close_order'] = order['limit']

    def check_stop_loss_and_limit(self, df, index):
        for order in self.orders:
            if order['lower_stop'] and order['lower_stop'] >= df.loc[index, 'Low']:
                # close order
                self.close_order(df, index, order['id'], order['lower_stop'])
                # Marker for Plot
                print("STOP LOSS")
                df.loc[index, 'close_order'] = order['lower_stop']
            if order['limit'] and order['limit'] <= df.loc[index, 'High']:
                self.close_order(df, index, order['id'], order['limit'])
                # Marker for Plot
                df.loc[index, 'close_order'] = order['limit']

    def current_gains(self, current_price):
        gains = self.cash

        for order in self.orders:
            if order['instrument'] == 'long':
                gains += order['units'] * current_price

            if order['instrument'] == 'short':
                profit_percentage = abs((order['buying_price'] / current_price))
                # print(profit_percentage, order['buying_price'], price)
                gains += order['units'] * order['buying_price'] * profit_percentage

        return gains

    def close_all_orders(self, df, price, index=None):
        for order in self.orders:
            self.close_order(df, index or df.index[-1], order['id'], price)



def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier) / multiplier