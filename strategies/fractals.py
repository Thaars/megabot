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
class FRACTALS:
    def __init__(self, df, pf):
        self.indicator = self.__class__.__name__
        self.df = df
        self.pf = pf
        self.config = definitions.FRACTALS
        # the maximum percentage share of the start cash in the portfolio to invest in each trade
        self.order_invest = self.config['order_invest']
        # determines, if the bullish fractal should be used as bearish signal and vice versa
        self.invert = self.config['invert']
        self.name_bullish = f'fractal_{definitions.FRACTALS_PERIOD}_bullish'
        self.name_bearish = f'fractal_{definitions.FRACTALS_PERIOD}_bearish'

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
        if row[self.name_bearish if self.invert else self.name_bullish] and len(self.pf.orders) == 0:
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
        if row[self.name_bullish if self.invert else self.name_bearish]:
            self.pf.close_position(line, index, row)
        # todo: stop loss behandeln bzw. vielleicht einfach nur das portfolio entscheiden lassen
        return False

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
