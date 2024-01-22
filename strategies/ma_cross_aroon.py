import json
import zlib
import pandas as pd
import definitions

# todo: add description
"""
 
"""


# these classes will hold all the required information for their part of the strategy
# it defines all possibilities and will generate random values based on that
# possible values and analyze the data for each tick
class MA_CROSS_AROON:
    def __init__(self, df, pf):
        self.indicator = self.__class__.__name__
        self.df = df
        self.pf = pf
        self.config = definitions.MA_CROSS_AROON
        # the maximum percentage share of the start cash in the portfolio to invest in each trade
        self.order_invest = self.config['order_invest']
        # the arron indicator which is responsible for buy must have at least a value of
        self.buy_aroon_min_value = self.config['buy_aroon_min_value']
        # the arron indicator which is responsible for sell must have at least a value of
        self.sell_aroon_min_value = self.config['sell_aroon_min_value']
        # sell early, if the current candle has made more than this percent profit
        self.candle_profit_sell_limit = self.config['candle_profit_sell_limit']
        # sell early, if the price has made more than this percent profit
        self.price_profit_sell_limit = self.config['price_profit_sell_limit']
        self.name_up = f'aroon_{definitions.AROON_PERIOD}_up'
        self.name_down = f'aroon_{definitions.AROON_PERIOD}_down'
        self.name_fast = f'ma_{definitions.MA_FAST_PERIOD}'
        self.name_slow = f'ma_{definitions.MA_SLOW_PERIOD}'
        self.name_golden_cross = f'ma_golden_cross_{definitions.MA_FAST_PERIOD}_{definitions.MA_SLOW_PERIOD}'
        self.name_death_cross = f'ma_death_cross_{definitions.MA_FAST_PERIOD}_{definitions.MA_SLOW_PERIOD}'

    def prepare(self):
        pass

    def analyze(self):
        for (line, (index, row)) in enumerate(self.df.iterrows()):
            if line == 0:
                self.pf.market_start_amount = row.close
            # remember the last price at the very end of the back testing for calculating stats
            if line + 1 == len(self.df):
                self.pf.market_end_amount = row.close
                self.pf.undo_all_open()

            # sell
            self.sell(line, index, row)
            # buy
            self.buy(line, index, row)

        return self.df, self.pf, self.config

    def buy(self, line, index, row):
        # todo: kaufen beim golden cross und upper aroon auf min value
        if self.do_we_have_a_golden_cross(line, index, row) is not True:
            return False
        if self.aroon_up_is_greater_than_min_buy_value(line, index, row) is not True:
            return False
        if len(self.pf.orders) > 0:
            return False

        # max invest of the portfolio cash in percent
        # the cash shouldn't be less than this
        buy_amount_of_cash = definitions.STARTING_AMOUNT / 100 * self.order_invest
        if self.pf.cash > buy_amount_of_cash:
            # create order
            order = self.pf.create_order(
                df=self.df,
                index=index,
                current_price=row['close'],
                target=None,
                # todo: stop loss einbauen und im portfolio aktivieren sowie in sell() berücksichtigen
                stop_loss=None,
                units=buy_amount_of_cash / row['close']
            )
            return True

        return False

    def sell(self, line, index, row):
        # todo: death cross
        if len(self.pf.orders) == 0:
            return False

        if self.price_has_min_performance(line, index, row, self.price_profit_sell_limit):
            self.pf.close_position(line, index, row)

        if self.candle_has_min_self_performance(line, index, row, self.candle_profit_sell_limit) \
                and self.price_has_min_performance(line, index, row, 1):
            self.pf.close_position(line, index, row)

        # if self.do_we_have_a_death_cross(line, index, row) is not True:
        #     return False
        if self.aroon_down_is_greater_than_min_sell_value(line, index, row) is not True:
            return False
        if self.aroon_up_has_crossed_aroon_down_upwards(line, index, row) is not True:
            return False

        self.pf.close_position(line, index, row)
        # todo: stop loss behandeln bzw. vielleicht einfach nur das portfolio entscheiden lassen
        return False

    def aroon_up_has_crossed_aroon_down_upwards(self, line, index, row):
        if row[self.name_up] < row[self.name_down] \
                and self.df.iloc[line - 1][self.name_up] < self.df.iloc[line - 1][self.name_down]:
            return True
        return False

    def aroon_down_is_greater_than_min_sell_value(self, line, index, row):
        if row[self.name_down] > self.sell_aroon_min_value:
            return True
        return False

    def do_we_have_a_death_cross(self, line, index, row):
        return row[self.name_death_cross]

    def do_we_have_a_golden_cross(self, line, index, row):
        return row[self.name_golden_cross]

    def aroon_up_is_greater_than_min_buy_value(self, line, index, row):
        if row[self.name_up] > self.buy_aroon_min_value:
            return True
        return False

    def candle_has_min_self_performance(self, line, index, row, limit):
        return self.get_performance_in_percent(row['open'], row['close']) > limit

    def price_has_min_performance(self, line, index, row, limit):
        if self.pf.get_first_order() is None:
            return False
        return self.get_performance_in_percent(self.pf.get_first_order()['buying_price'], row['close']) > limit

    def get_performance_in_percent(self, old_value, new_value):
        return ((new_value - old_value) / old_value) * 100

    def get_preparation_values(self):
        return {
            'name': self.get_name(),
            'indicator': self.indicator,
            'hash': hash(self)
        }

    def get_name(self):
        return self.indicator

    def __hash__(self):
        return zlib.adler32(self.get_name().encode('UTF-8')) & 0xffffffff
