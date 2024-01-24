#!/usr/bin/python
# -*- encoding: utf-8 -*-

__author__ = 'Jan Olschewski, Ingo Volkmann'

import datetime

from strategies.price_breakout import PRICE_BREAKOUT

APP_VERSION = "0.0.1"

TRADOVATE_URL = "https://live.tradovateapi.com/v1"
TRADOVATE_WEBSOCKET_URL = "wss://md.tradovateapi.com/v1/websocket"
# TRADOVATE_MARKET_DATA_URL = "https://demo.tradovateapi.com/v1"

STOP_LOSS_LEVEL = 98.5
LIMIT_LEVEL = 105
STARTING_AMOUNT = 2000
DAYS = 365
INDICATORS = list()
# 0,1% at binance
COMMISSION_FACTOR = 0.001
# $0.25 at Tradovate
COMMISSION_VALUE = 0.25

AROON_PERIOD = 25
MA_FAST_PERIOD = 7
MA_SLOW_PERIOD = 26
FRACTALS_PERIOD = 5

# 02/2022 - 12/2022
# HISTORICAL_DATA_FROM = '01 Feb 2022'
# HISTORICAL_DATA_TO = '31 Dec 2022'
# START_DATE = datetime.datetime(year=2022, month=2, day=1, hour=0, minute=0)
# END_DATE = datetime.datetime(year=2022, month=12, day=31, hour=23, minute=59)
# 11/2021 - 12/2022
# HISTORICAL_DATA_FROM = '01 Nov 2021'
# HISTORICAL_DATA_TO = '31 Dec 2022'
# START_DATE = datetime.datetime(year=2021, month=11, day=1, hour=0, minute=0)
# END_DATE = datetime.datetime(year=2022, month=12, day=31, hour=23, minute=59)
# 2019 - 2023
# HISTORICAL_DATA_FROM = '01 Jan 2019'
# HISTORICAL_DATA_TO = '31 Dec 2023'
# START_DATE = datetime.datetime(year=2019, month=1, day=1, hour=0, minute=0)
# END_DATE = datetime.datetime(year=2023, month=12, day=31, hour=23, minute=59)
# 2023
# HISTORICAL_DATA_FROM = '01 Jan 2023'
# HISTORICAL_DATA_TO = '31 Dec 2023'
# START_DATE = datetime.datetime(year=2023, month=1, day=1, hour=0, minute=0)
# END_DATE = datetime.datetime(year=2023, month=12, day=31, hour=23, minute=59)
# 2022
# HISTORICAL_DATA_FROM = '1 Jan 2022'
# HISTORICAL_DATA_TO = '31 Dec 2022'
# START_DATE = datetime.datetime(year=2022, month=1, day=1, hour=0, minute=0)
# END_DATE = datetime.datetime(year=2022, month=12, day=31, hour=23, minute=59)
# 01/2022
HISTORICAL_DATA_FROM = '1 Jan 2022'
HISTORICAL_DATA_TO = '31 Jan 2022'
START_DATE = datetime.datetime(year=2022, month=1, day=1, hour=0, minute=0)
END_DATE = datetime.datetime(year=2022, month=1, day=31, hour=23, minute=59)
# 2021
# HISTORICAL_DATA_FROM = '1 Jan 2021'
# HISTORICAL_DATA_TO = '31 Dec 2021'
# START_DATE = datetime.datetime(year=2021, month=1, day=1, hour=0, minute=0)
# END_DATE = datetime.datetime(year=2021, month=12, day=31, hour=23, minute=59)
# 2020
# HISTORICAL_DATA_FROM = '01 Jan 2020'
# HISTORICAL_DATA_TO = '31 Dec 2020'
# START_DATE = datetime.datetime(year=2020, month=1, day=1, hour=0, minute=0)
# END_DATE = datetime.datetime(year=2020, month=12, day=31, hour=23, minute=59)
# 2019
# HISTORICAL_DATA_FROM = '01 Jan 2019'
# HISTORICAL_DATA_TO = '31 Dec 2019'
# START_DATE = datetime.datetime(year=2019, month=1, day=1, hour=0, minute=0)
# END_DATE = datetime.datetime(year=2019, month=12, day=31, hour=23, minute=59)

PRICE_BREAKOUT_CONFIG = {
    # long|short|both
    'trade_type': 'long',
    # number of past candles to take into account for decisions
    'number_of_past_candles': 15,
    # the (lower (short) or upper (long)) wick may not be larger than this value in percent of the candle body
    'max_wick_in_percent': 15,
    # the current candle body must be at least n times larger than the largest body of the n previous candles
    'min_prev_body_diff_factor': 2,
    # the current candle body may not be greater that n times of the largest body of the last n previous candles
    'max_prev_body_diff_factor': 4,
    # if set to True, the highest high and lowest low checks will be used
    # if set to false, the current candle body must not be higher or lower than the previous ones
    'use_highest_high_and_lowest_low': True,
    # use the largest body instead of the current body for target and stop loss
    # this will disable the next target and stop loss factor settings
    'use_largest_body_as_target_and_stop_loss': False,
    # the target is n times the current candle body
    'target_diff_from_candle_factor': 2.2,
    # the stop loss is n times the current candle body
    'stop_loss_diff_from_candle_factor': 1,
    # the stop loss and target will be reached, if the price exceeds these values
    # the price is lower than low|close for long trades
    'stop_loss_long_limit_key': 'low',
    # the price is higher than high|close for long trades
    'target_long_limit_key': 'high',
    # the price is higher than high|close for short trades
    'stop_loss_short_limit_key': 'high',
    # the price is lower than low|close for short trades
    'target_short_limit_key': 'low',
}

PRICE_MINI_WICKS_CONFIG = {
    # long|short|both
    'trade_type': 'long',
    # number of past candles to take into account for decisions
    'number_of_past_candles': 10,
    # the (lower (short) or upper (long)) wick may not be larger than this value in percent of the candle body
    'max_positive_wick_in_percent': 5,
    # the (upper (short) or lower (long)) wick may not be larger than this value in percent of the candle body
    'max_negative_wick_in_percent': 5,
    # the current candle body must be at least n times larger than the largest body of the n previous candles
    'min_prev_body_diff_factor': 0.5,
    # the current candle body may not be greater that n times of the largest body of the last n previous candles
    'max_prev_body_diff_factor': 2,
    # the target is n times the current candle body
    'target_diff_from_candle_factor': 4,
    # the stop loss is n times the current candle body
    'stop_loss_diff_from_candle_factor': 1,
    # the stop loss and target will be reached, if the price exceeds these values
    # the price is lower than low|close for long trades
    'stop_loss_long_limit_key': 'low',
    # the price is higher than high|close for long trades
    'target_long_limit_key': 'high',
    # the price is higher than high|close for short trades
    'stop_loss_short_limit_key': 'high',
    # the price is lower than low|close for short trades
    'target_short_limit_key': 'low',
}

PRICE_QUICK_DOJI_CONFIG = {
    # long|short|both
    'trade_type': 'long',
    # number of past candles to take into account for decisions
    'max_body_in_percent': 15,
    # the wicks may not be smaller than this value in percent of the candle body
    'min_wick_in_percent': 1,
    # the wicks must be differ from each other for at least n percent
    'wick_diff_in_percent': 40,
    # use wicks as target and stop loss
    'use_wicks_as_target_and_stop_loss': False,
}

PRICE_BUY_RED_CONFIG = {
    # the maximum percentage part of the start cash in the portfolio to invest in each cycle
    'cycle_max_invest_of_cash_in_percent': 10,
    # the number of dollars which will be invested for each order
    'order_invest': 20,
    # the multiplier to append more cash to a buy when the next red candle is much longer
    # the lower the price, the more the invest
    'order_invest_factor': 20,
    # a factor to increase the sell price related to the buying price in percent
    'sell_price_factor_in_percent': 5,
    # the number of candles from the last buy until the cycle goes on hold
    'candle_limit_until_hold': 50,
    # the number of candles from the last buy and for cycles on hold until the sell price
    # will not be longer cycle start price, it will be changed to the cycle average buying price
    'candle_limit_until_sell_for_average_price': 100
}

AROON = {
    # the maximum percentage share of the start cash in the portfolio to invest in each trade
    'order_invest': 10,
    # the arron indicator which is responsible for sell must have at least a value of
    'sell_aroon_min_value': 95
}

MA_CROSS_AROON = {
    # the maximum percentage share of the start cash in the portfolio to invest in each trade
    'order_invest': 50,
    # the arron indicator which is responsible for buy must have at least a value of
    'buy_aroon_min_value': 0,
    # the arron indicator which is responsible for sell must have at least a value of
    'sell_aroon_min_value': 0,
    # sell early, if the current candle has made more than this percent profit
    'candle_profit_sell_limit': 5,
    # sell early, if the price has made more than this percent profit
    'price_profit_sell_limit': 50
}

FRACTALS = {
    # the maximum percentage share of the start cash in the portfolio to invest in each trade
    'order_invest': 50,
    # determines, if the bullish fractal should be used as bearish signal and vice versa
    'invert': True
}


# todo: commission
#   cash commission
#   tick commission - stimmen tick size und tick value und die logik dahinter?
# todo: retest mit anderen Zeiträumen
# todo: testen von verschiedenen Parametern

# USED_STRATEGY = 'price_breakout'
# USED_STRATEGY = 'price_mini_wicks'
# USED_STRATEGY = 'price_quick_doji'
# USED_STRATEGY = 'price_buy_red'
# USED_STRATEGY = 'aroon'
# USED_STRATEGY = 'ma_cross_aroon'
USED_STRATEGY = 'fractals'
TIMEFRAME = "30m"
SYMBOL = 'BTCUSDT'
TICK_SIZE = 0.25
TICK_VALUE = 1.25
USE_TRADING_BREAKS = False
# @see https://community.tradovate.com/t/how-to-detect-whether-the-a-future-market-is-open-or-not/3575/4?u=ingo
# @see https://www.tradovate.com/resources/markets/?p=MES
# @see https://www.cmegroup.com/markets/equities/sp/micro-e-mini-sandp-500.contractSpecs.html
# @see https://tradovate.zendesk.com/hc/en-us/articles/115002511608-What-hours-are-day-night-and-initial-margins-available-
# todo: implement public holidays (maybe by auto importing because of different weekdays each year)
TRADING_BREAKS = [{
    'symbols': [
        'MESM2'
    ],
    'breaks': [
        {
            'from': '00:00',
            'to': '07:00'
        },
        {
            'from': '15:00',
            'to': '23:59'
        }
    ]
}]

# PLOT = True
PLOT = False

TIMEFRAME_MINUTE_MAPPING = {
    '1m': 1,
    '3m': 3,
    '5m': 5,
    '10m': 10,
    '15m': 15,
    '30m': 30,
    '1h': 60,
    '2h': 120,
    '4h': 240,
    "1d": 1440,
}


