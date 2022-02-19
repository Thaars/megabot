#!/usr/bin/python
# -*- encoding: utf-8 -*-

__author__ = 'Jan Olschewski, Ingo Volkmann'

from datetime import date

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
# SYMBOL = 'BNBBTC'
SYMBOL = 'GC=F'

# PLOT = True
PLOT = False
