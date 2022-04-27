import warnings
import zlib
import pandas as pd
from definitions import *

"""
the shorter wick of the doji determines the trading type (long|short)
only the next candle is traded with open and close price (this can be configured if necessary)
or the wicks determine target and stop loss 
"""

# todo: mögliche indikatoren
#   kurzer Docht zeigt Richtung der nächsten Kerze an - nur nächste Kerze handlen
#   langer Docht zeigt Richtung der nächsten Kerze an - nur nächste Kerze handeln
#   vorherige Kerze zeigt Richtung der nächsten Kerze an - nur nächste Kerze handeln
#   Verhältnis zwischen langem und kurzem Docht darf nicht fast gleich sein


# these classes will hold all the required information for their part of the strategy
# it defines all possibilities and will generate random values based on that
# possible values and analyze the data for each tick
class PRICE_QUICK_DOJI:
    def __init__(self, df, pf):
        self.indicator = self.__class__.__name__
        self.df = df
        self.pf = pf
        self.rules = {
            'long': ["bullish"],
            'short': ["bearish"]
        }
        self.config = PRICE_QUICK_DOJI_CONFIG
        # long|short|both
        self.trade_type = self.config['trade_type']
        # number of past candles to take into account for decisions
        self.max_body_in_percent = self.config['max_body_in_percent']
        # the wicks may not be smaller than this value in percent of the candle body
        self.min_wick_in_percent = self.config['min_wick_in_percent']
        # the wicks must be differ from each other for at least n percent
        self.wick_diff_in_percent = self.config['wick_diff_in_percent']
        # use wicks as target and stop loss
        self.use_wicks_as_target_and_stop_loss = self.config['use_wicks_as_target_and_stop_loss']

    def prepare(self):
        pass
        # # get random rule
        # rules_by_trade_type = self.rules[self.trade_type]
        # random.shuffle(rules_by_trade_type)
        # self.current_rule = rules_by_trade_type[0]

    def analyze(self):
        for (line, (index, row)) in enumerate(self.df.iterrows()):
            if line == 0:
                self.pf.market_start_amount = row.close
            self.pf.close_position(
                line,
                index,
                row
            )

            # check for opening position
            # is the current candle a doji?
            body = abs(row['close'] - row['open'])
            candle = abs(row['high'] - row['low'])

            if body > 0 and candle > 0 and body * 100 / candle <= self.max_body_in_percent:

                # todo: erwische ich hier alles?
                #   wenn der kleinere docht oben ist, wäre das theoretisch bullish,
                #   wenn aber gleichzeitig close < open ist, fällt das in bearish
                #   und würde dort eigentlich die falsche richtung vorgeben
                #   das müsste mal mit parametern getestet werden, vielleicht funktioniert das ja nur aufgrund des logikfehlers

                if row['close'] > row['open']:
                    upper_shadow = row['high'] - row['close']
                    lower_shadow = row['open'] - row['low']
                else:
                    upper_shadow = row['high'] - row['open']
                    lower_shadow = row['close'] - row['low']

                # bullish
                if (self.trade_type == 'long' or self.trade_type == 'both') and upper_shadow < lower_shadow:
                    self.rule_long_bullish(line, index, row, body)

                # bearish
                if (self.trade_type == 'short' or self.trade_type == 'both') and lower_shadow < upper_shadow:
                    self.rule_short_bearish(line, index, row, body)

            # close all and do not open any new positions at the very end of the back testing
            if line + 1 == len(self.df):
                self.pf.market_end_amount = row.close
                self.pf.close_position(line, index, row, undo_all_open=True)

        return self.df, self.pf, self.config

    def rule_long_bullish(self, line, index, row, body):
        if row['close'] > row['open']:
            # the upper shadow may not be greater than n% of the body
            upper_shadow = row['high'] - row['close']
            # and the shadows must differ from each other for at least n%
            lower_shadow = row['open'] - row['low']
            diff = abs(((upper_shadow * 100) / body) - ((lower_shadow * 100) / body))
            if ((upper_shadow * 100) / body) > self.min_wick_in_percent and diff > self.wick_diff_in_percent:
                # open long position
                target = 'candle:next:close'
                stop_loss = row['low']
                if self.use_wicks_as_target_and_stop_loss:
                    target = row['high']
                    stop_loss = row['low']
                self.pf.create_order(
                    df=self.df,
                    index=index,
                    current_price=row['close'],
                    target=target,
                    stop_loss=stop_loss,
                    trade_type='long'
                )
                return True
        return False

    def rule_short_bearish(self, line, index, row, body):
        if row['close'] < row['open']:
            # the lower shadow may not be greater than n% of the body
            lower_shadow = row['close'] - row['low']
            # and the shadows must differ from each other for at least n%
            upper_shadow = row['high'] - row['open']
            diff = abs(((upper_shadow * 100) / body) - ((lower_shadow * 100) / body))
            if ((lower_shadow * 100) / body) > self.min_wick_in_percent and diff > self.wick_diff_in_percent:
                # open short position
                target = 'candle:next:close'
                stop_loss = row['high']
                if self.use_wicks_as_target_and_stop_loss:
                    target = row['low']
                    stop_loss = row['high']
                self.pf.create_order(
                    df=self.df,
                    index=index,
                    current_price=row['close'],
                    target=target,
                    stop_loss=stop_loss,
                    trade_type='short'
                )
                return True
        return False

    def get_preparation_values(self):
        return {
            'name': self.get_name(),
            'indicator': self.indicator,
            # 'rule': f'{self.current_rule}',
            'hash': hash(self)
        }

    def get_name(self):
        return self.indicator

    def __hash__(self):
        return zlib.adler32(self.get_name().encode('UTF-8')) & 0xffffffff
