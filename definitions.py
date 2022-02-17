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

HISTORICAL_DATA_FROM = '1 Jan 2021'
HISTORICAL_DATA_TO = '1 Jan 2022'

START_DATE = date(2021, 12, 19)
END_DATE = date(2022, 2, 17)
TIMEFRAME = "5m"
SYMBOL = 'GC=F'

PLOT = True
