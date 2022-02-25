import zlib
import pandas as pd
from definitions import *

"""
Candle Wicks may both be max. 5 or 10 percent of the Body length
Body must not be more than twice the size of the largest body of the last 5 candles
Stop Loss: 0.1x Candle Body
Target: 1x candle body
Short + Long
5m, 10m, 15m test if necessary also sometimes 1m or 3m
   Gold: possibly 1m or 2m, because at 5m always longer wicks were seen
   BTC: seems to be quite good with 5m
"""


# these classes will hold all the required information for their part of the strategy
# it defines all possibilities and will generate random values based on that
# possible values and analyze the data for each tick
class PRICE_MINI_WICKS:
    def __init__(self, df, pf):
        self.indicator = self.__class__.__name__
        self.df = df
        self.pf = pf
        self.rules = {
            'long': ["bullish"],
            'short': ["bearish"]
        }
        self.config = PRICE_MINI_WICKS_CONFIG
        # long|short|both
        self.trade_type = self.config['trade_type']
        # number of past candles to take into account for decisions
        self.number_of_past_candles = self.config['number_of_past_candles']
        # the (upper (short) or lower (long)) wick may not be larger than this value in percent of the candle body
        self.max_negative_wick_in_percent = self.config['max_negative_wick_in_percent']
        # the (lower (short) or upper (long)) wick may not be larger than this value in percent of the candle body
        self.max_positive_wick_in_percent = self.config['max_positive_wick_in_percent']
        # the current candle body must be at least n times larger than the largest body of the n previous candles
        self.min_prev_body_diff_factor = self.config['min_prev_body_diff_factor']
        # the current candle body may not be greater than n times of the largest body of the last n previous candles
        self.max_prev_body_diff_factor = self.config['max_prev_body_diff_factor']
        # the target is n times the current candle body
        self.target_diff_from_candle_factor = self.config['target_diff_from_candle_factor']
        # the stop loss is n times the current candle body
        self.stop_loss_diff_from_candle_factor = self.config['stop_loss_diff_from_candle_factor']
        # the stop loss and target will be reached, if the price exceeds these values
        # the price is lower than low|close for long trades
        self.stop_loss_long_limit_key = self.config['stop_loss_long_limit_key']
        # the price is higher than high|close for long trades
        self.target_long_limit_key = self.config['target_long_limit_key']
        # the price is higher than high|close for short trades
        self.stop_loss_short_limit_key = self.config['stop_loss_short_limit_key']
        # the price is lower than low|close for short trades
        self.target_short_limit_key = self.config['target_short_limit_key']

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
                row,
                stop_loss_long_limit_key=self.stop_loss_long_limit_key,
                target_long_limit_key=self.target_long_limit_key,
                stop_loss_short_limit_key=self.stop_loss_short_limit_key,
                target_short_limit_key=self.target_short_limit_key
            )

            # check for opening position
            # we need at least n candles
            if line > self.number_of_past_candles:

                # compare with the current candle
                body = abs(row['close'] - row['open'])
                if body > 0 \
                        and row[f'largest_body_{self.number_of_past_candles}'] * self.min_prev_body_diff_factor < body \
                        < row[f'largest_body_{self.number_of_past_candles}'] * self.max_prev_body_diff_factor:

                    # bullish
                    if self.trade_type == 'long' or self.trade_type == 'both':
                        self.rule_long_bullish(line, index, row, body)

                    # bearish
                    if self.trade_type == 'short' or self.trade_type == 'both':
                        self.rule_short_bearish(line, index, row, body)

            # close all and do not open any new positions at the very end of the back testing
            if line + 1 == len(self.df):
                self.pf.market_end_amount = row.close
                self.pf.close_position(line, index, row, undo_all_open=True)

        return self.df, self.pf, self.config

    def rule_long_bullish(self, line, index, row, body):
        if row['close'] > row['open']:
            # the upper and the lower shadows may not be greater than n% of the body
            upper_shadow = row['high'] - row['close']
            lower_shadow = row['open'] - row['low']
            if ((upper_shadow * 100) / body) < self.max_positive_wick_in_percent \
                    and ((lower_shadow * 100) / body) < self.max_negative_wick_in_percent:
                # open long position
                target = row['close'] + (body * self.target_diff_from_candle_factor)
                stop_loss = row['close'] - (body * self.stop_loss_diff_from_candle_factor)
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
            upper_shadow = row['high'] - row['open']
            if ((lower_shadow * 100) / body) < self.max_positive_wick_in_percent \
                    and ((upper_shadow * 100) / body) < self.max_negative_wick_in_percent:
                # open short position
                target = row['close'] - (body * self.target_diff_from_candle_factor)
                stop_loss = row['close'] + (body * self.stop_loss_diff_from_candle_factor)
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
