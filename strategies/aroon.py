import json
import zlib
import pandas as pd
import definitions

# todo: add description
"""
 
"""

STATE_RUNNING = 'running'
STATE_HOLD = 'hold'
STATE_DEAD = 'dead'


# these classes will hold all the required information for their part of the strategy
# it defines all possibilities and will generate random values based on that
# possible values and analyze the data for each tick
class AROON:
    def __init__(self, df, pf):
        self.indicator = self.__class__.__name__
        self.df = df
        self.pf = pf
        self.config = definitions.AROON
        # the maximum percentage share of the start cash in the portfolio to invest in each trade
        self.order_invest = self.config['order_invest']
        # the arron indicator which is responsible for sell must have at least a value of
        self.sell_aroon_min_value = self.config['sell_aroon_min_value']
        self.name_up = f'aroon_{definitions.AROON_PERIOD}_up'
        self.name_down = f'aroon_{definitions.AROON_PERIOD}_down'

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
        # todo: wenn der lower aroon den upper aufsteigend durchkreuzt hat, kaufen
        if row[self.name_up] < row[self.name_down] \
                and self.df.iloc[line - 1][self.name_up] > self.df.iloc[line - 1][self.name_down] \
                and len(self.pf.orders) == 0:
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
        # todo: wenn der upper aroon den lower aufsteigend durchkreuzt hat, verkaufen
        if row[self.name_up] > row[self.name_down] \
                and self.df.iloc[line - 1][self.name_up] < self.df.iloc[line - 1][self.name_down] \
                and row[self.name_up] > self.sell_aroon_min_value:
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
