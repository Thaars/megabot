import zlib
import pandas as pd


# these classes will hold all the required information for their part of the strategy
# it defines all possibilities and will generate random values based on that
# possible values and analyze the data for each tick
class PRICE_OUTBREAK:
    def __init__(self, df, pf, trade_type='long'):
        self.indicator = self.__class__.__name__
        self.df = df
        self.pf = pf
        self.trade_type = trade_type
        self.rules = {
            'long': ["bullish"],
            'short': ["bearish"]
        }
        # number of past candles to take into account for decisions
        self.number_of_past_candles = 20
        # the (lower (short) or upper (long)) wick may not be larger than this value in percent of the candle body
        self.max_wick_in_percent = 5
        # the current candle body must be at least n times larger than the largest body of the n previous candles
        self.min_prev_body_diff_factor = 1.5
        # the current candle body may not be greater that n times of the largest body of the last n previous candles
        self.max_prev_body_diff_factor = 3
        # if set to True, the highest high and lowest low checks will be ignored
        # so the current candle body must not be higher or lower than the previous ones
        self.dont_use_highest_high_and_lowest_low = True
        # use the largest body instead of the current body for target and stop loss
        # this will disable the next target and stop loss factor settings
        self.use_largest_body_as_target_and_stop_loss = False
        # the target is n times the current candle body
        self.target_diff_from_candle_factor = 3
        # the stop loss is n times the current candle body
        self.stop_loss_diff_from_candle_factor = 1.5
        # the stop loss and target will be reached, if the price exceeds these values
        # the price is lower than low|close for long trades
        self.stop_loss_long_limit_key = 'low'
        # the price is higher than high|close for long trades
        self.target_long_limit_key = 'high'
        # the price is higher than high|close for short trades
        self.stop_loss_short_limit_key = 'high'
        # the price is lower than low|close for short trades
        self.target_short_limit_key = 'low'

    def prepare(self):
        pass
        # # get random rule
        # rules_by_trade_type = self.rules[self.trade_type]
        # random.shuffle(rules_by_trade_type)
        # self.current_rule = rules_by_trade_type[0]

    def analyze(self):
        # todo: es müssen Zeiträume gewählt werden können (2 Wochen oder so), die dann zufällig durchgetestet werden
        #     das stellt quasi direkt den Retest dar

        # todo: vielleicht ist es besser, wenn Target und Stop Loss nur so groß wären wie die größte Kerze der letzzten 20 Tage
        #   extreme Ausbrüche können sonst zu hohen Verlusten führen
        #     z.b. 2% Kerze - wenn die 2% nicht erreicht werden, kann es sein, dass die 2% in die Gegenrichtung erreicht werden
        #   oder wenigstens anteilig, dass man das abhängig von der Größe der Ausbruchskerze im Verhältnis zu der größten der letzten 20 Kerzen macht

        # todo return bearish signal as well
        #      ggf. dynamisch stop loss nachziehen und target erhöhen
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

                # compare with the current candle - the current must be n times greater
                body = abs(row['close'] - row['open'])
                if row[f'largest_body_{self.number_of_past_candles}'] * self.min_prev_body_diff_factor \
                        < body \
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

        return self.df, self.pf

    def rule_long_bullish(self, line, index, row, body):
        highest_high = row[f'highest_high_{self.number_of_past_candles}']
        if row['close'] > row['open']:
            # close must be greater than the highest high
            if self.dont_use_highest_high_and_lowest_low and row['close'] > highest_high:
                # the upper shadow may not be greater than n% of the body
                shadow = row['high'] - row['close']
                if ((shadow * 100) / body) < self.max_wick_in_percent:
                    # open long position
                    target = row['close'] + (body * self.target_diff_from_candle_factor)
                    stop_loss = row['close'] - (body * self.stop_loss_diff_from_candle_factor)
                    if self.use_largest_body_as_target_and_stop_loss:
                        target = row['close'] + row[f'largest_body_{self.number_of_past_candles}']
                        stop_loss = row['close'] - row[f'largest_body_{self.number_of_past_candles}']
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
        lowest_low = row[f'lowest_low_{self.number_of_past_candles}']
        if row['close'] < row['open']:
            # close must be lower than the lowest low
            if self.dont_use_highest_high_and_lowest_low or row['close'] < lowest_low:
                # the lower shadow may not be greater than n% of the body
                shadow = row['close'] - row['low']
                if ((shadow * 100) / body) < self.max_wick_in_percent:
                    # open short position
                    target = row['close'] - (body * self.target_diff_from_candle_factor)
                    stop_loss = row['close'] + (body * self.stop_loss_diff_from_candle_factor)
                    if self.use_largest_body_as_target_and_stop_loss:
                        target = row['close'] - row[f'largest_body_{self.number_of_past_candles}']
                        stop_loss = row['close'] + row[f'largest_body_{self.number_of_past_candles}']
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
