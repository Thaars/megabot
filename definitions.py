#!/usr/bin/python
# -*- encoding: utf-8 -*-

__author__ = 'Jan Olschewski, Ingo Volkmann'

from datetime import date

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASS = "godiv"
MYSQL_DB = "megabot"

STOP_LOSS_LEVEL = 98.5
LIMIT_LEVEL = 105
STARTING_AMOUNT = 100
DAYS = 365
INDICATORS = list()
COMMISSION = 0.000 # 0,1% at binance

# HISTORICAL_DATA_FROM = '8 Dec 2021'
# HISTORICAL_DATA_TO = '17 Feb 2022'
# START_DATE = date(2021, 12, 8)
# END_DATE = date(2022, 2, 17)
HISTORICAL_DATA_FROM = '3 Jan 2021'
HISTORICAL_DATA_TO = '31 Dec 2021'
START_DATE = date(2021, 1, 1)
END_DATE = date(2021, 12, 31)

TIMEFRAME = "5m"
# SYMBOL = 'BTCUSDT'

PRICE_BREAKOUT_CONFIG = {
    'strategy': 'price_breakout',
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

# todo: config irgendwie persistieren zusammen mit den Ergebnissen, damit man das auch alles später wiederherstellen kann
#   ggf. auch einfach in Dateien schreiben - oder in DB - vielleicht sogar zusammen mit dem Plot?

# todo: Gold retest mit anderen Zeiträumen

SYMBOL = 'GC=F'
TICK_SIZE = 0.1
TICK_VALUE = 10
# USE_TRADING_BREAKS = True
USE_TRADING_BREAKS = False
TRADING_BREAKS = [
    {
        'from': '16:00',
        'to': '18:00'
    },
    {
        'from': '08:00',
        'to': '09:00'
    }
]

# PLOT = True
PLOT = False
