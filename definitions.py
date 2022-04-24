#!/usr/bin/python
# -*- encoding: utf-8 -*-

__author__ = 'Jan Olschewski, Ingo Volkmann'

import datetime

from strategies.price_breakout import PRICE_BREAKOUT

APP_VERSION = "0.0.1"

TRADOVATE_URL = "https://live.tradovateapi.com/v1"
TRADOVATE_WEBSOCKET_URL = "wss://md.tradovateapi.com/v1/websocket"
# TRADOVATE_MARKET_DATA_URL = "https://demo.tradovateapi.com/v1"

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASS = "godiv"
MYSQL_DB = "megabot"

STOP_LOSS_LEVEL = 98.5
LIMIT_LEVEL = 105
STARTING_AMOUNT = 100
DAYS = 365
INDICATORS = list()
# 0,1% at binance
COMMISSION_FACTOR = 0.000
# $0.25 at Tradovate
COMMISSION_VALUE = 0.25

HISTORICAL_DATA_FROM = '15 Mar 2022'
HISTORICAL_DATA_TO = '15 Apr 2022'
START_DATE = datetime.datetime(year=2022, month=1, day=1, hour=0, minute=0)
END_DATE = datetime.datetime(year=2022, month=4, day=20, hour=0, minute=0)
# HISTORICAL_DATA_FROM = '3 Jan 2021'
# HISTORICAL_DATA_TO = '31 Dec 2021'
# START_DATE = datetime.datetime(year=2021, month=1, day=3, hour=0, minute=0)
# END_DATE = datetime.datetime(year=2021, month=1, day=31, hour=23, minute=59)

PRICE_BREAKOUT_CONFIG = {
    # long|short|both
    'trade_type': 'long',
    # number of past candles to take into account for decisions
    'number_of_past_candles': 20,
    # the (lower (short) or upper (long)) wick may not be larger than this value in percent of the candle body
    'max_wick_in_percent': 25,
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
    'target_diff_from_candle_factor': 2,
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
    'number_of_past_candles': 5,
    # the (lower (short) or upper (long)) wick may not be larger than this value in percent of the candle body
    'max_positive_wick_in_percent': 2,
    # the (upper (short) or lower (long)) wick may not be larger than this value in percent of the candle body
    'max_negative_wick_in_percent': 2,
    # the current candle body must be at least n times larger than the largest body of the n previous candles
    'min_prev_body_diff_factor': 0.1,
    # the current candle body may not be greater that n times of the largest body of the last n previous candles
    'max_prev_body_diff_factor': 3,
    # the target is n times the current candle body
    'target_diff_from_candle_factor': 2,
    # the stop loss is n times the current candle body
    'stop_loss_diff_from_candle_factor': 0.1,
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
    'trade_type': 'both',
    # number of past candles to take into account for decisions
    'max_body_in_percent': 15,
    # the wicks may not be smaller than this value in percent of the candle body
    'min_wick_in_percent': 1,
    # the wicks must be differ from each other for at least n percent
    'wick_diff_in_percent': 40,
    # use wicks as target and stop loss
    'use_wicks_as_target_and_stop_loss': False,
}

# todo: commission
#   cash commission
#   tick commission - stimmen tick size und tick value und die logik dahinter?
# todo: retest mit anderen Zeiträumen
# todo: testen von verschiedenen Parametern

USED_STRATEGY = 'price_breakout'
# USED_STRATEGY = 'price_mini_wicks'
# USED_STRATEGY = 'price_quick_doji'
TIMEFRAME = "1m"
SYMBOL = 'MESM2'
TICK_SIZE = 0.25
TICK_VALUE = 1.25
USE_TRADING_BREAKS = True
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


