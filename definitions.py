#!/usr/bin/python
# -*- encoding: utf-8 -*-

__author__ = 'Jan Olschewski, Ingo Volkmann'

from datetime import date

STOP_LOSS_LEVEL = 98.5
LIMIT_LEVEL = 105
STARTING_AMOUNT = 100
DAYS = 365
INDICATORS = list()
COMMISSION = 0.001 # 0,1% at binance

BINANCE_DATA_FROM = '1 Jan 2021'
BINANCE_DATA_TO = '1 Jan 2022'

START_DATE = date(2021, 2, 1)  # start date
END_DATE = date(2021, 6, 1)  # edate = date(2018, 8, 15)
TIMEFRAME = "5m"
SYMBOL = 'BTCUSDT'

PLOT = False
