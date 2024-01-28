#!/usr/bin/python
# -*- encoding: utf-8 -*-

__author__ = 'Jan Olschewski, Ingo Volkmann'


# IMPORTS
import json

import pandas as pd
import math
import os.path
import time

import asyncio
import websockets
from binance.client import Client
from datetime import timedelta, datetime, date
from dateutil import parser
import yfinance as yf
from pandas_finance import Equity

# API
import definitions
from api_key import *
from db import DB

from tradovate.tradovate_api_client import Client as TradovateClient
from tradovate.tradovate_api_client import AuthenticatedClient
from tradovate.tradovate_api_client.api.authentication import access_token_request
from tradovate.tradovate_api_client.models import AccessTokenRequest

binance_client = Client(api_key=BINANCE_API_KEY, api_secret=BINANCE_API_SECRET)


# FUNCTIONS
def minutes_of_new_data(symbol, kline_size, data, source):
    old = None
    new = None
    if len(data) > 0:
        old = parser.parse(data["timestamp"].iloc[-1])
    elif source == "binance":
        old = datetime.strptime(definitions.HISTORICAL_DATA_FROM, '%d %b %Y')
    if source == "binance":
        new = datetime.strptime(definitions.HISTORICAL_DATA_TO, '%d %b %Y')
        # new = pd.to_datetime(binance_client.get_klines(symbol=symbol, interval=kline_size)[-1][0], unit='ms')
    return old, new


def get_all_binance(symbol, kline_size, save=True):
    filename = 'data_with_indicators/%s-%s-%s-%s-data.csv' % (
        symbol, kline_size, definitions.HISTORICAL_DATA_FROM, definitions.HISTORICAL_DATA_TO
    )
    if os.path.isfile(filename):
        data_df = pd.read_csv(filename)
    else:
        data_df = pd.DataFrame()
        oldest_point, newest_point = minutes_of_new_data(symbol, kline_size, data_df, source="binance")
        delta_min = (newest_point - oldest_point).total_seconds()/60
        available_data = math.ceil(delta_min/definitions.TIMEFRAME_MINUTE_MAPPING[kline_size])
        if oldest_point == datetime.strptime(definitions.HISTORICAL_DATA_FROM, '%d %b %Y'):
            print('Downloading all available %s data for %s. Be patient..!' % (kline_size, symbol))
        else:
            print('Downloading %d minutes of new data available for %s, i.e. %d instances of %s data.' % (delta_min, symbol, available_data, kline_size))
        klines = binance_client.get_historical_klines(symbol, kline_size, oldest_point.strftime("%d %b %Y %H:%M:%S"), newest_point.strftime("%d %b %Y %H:%M:%S"))
        data = pd.DataFrame(klines, columns=['datetime', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore'])
        data['datetime'] = pd.to_datetime(data['datetime'], unit='ms')
        if len(data_df) > 0:
            temp_df = pd.DataFrame(data)
            data_df = data_df.append(temp_df)
        else:
            data_df = data
        data_df.set_index('datetime', inplace=True)
        if save:
            data_df.to_csv(filename, sep=";")
        print('All caught up..!')
    return filename


def get_stock_data(symbol, timeframe="5m"):
    filename = 'data_with_indicators/%s-%s-%s-%s-data.csv' % (
        symbol, timeframe, definitions.HISTORICAL_DATA_FROM, definitions.HISTORICAL_DATA_TO
    )
    if os.path.isfile(filename):
        data_df = pd.read_csv(filename)
    else:
        to_date = date.today().strftime('%d %b %Y')
        from_date = (date.today() - timedelta(days=60)).strftime('%d %b %Y')
        filename = 'data_with_indicators/%s-%s-%s-%s-data.csv' % (
            symbol, timeframe, from_date, to_date
        )
        if os.path.isfile(filename):
            data_df = pd.read_csv(filename)
        else:
            period_map = {"15m": "60d", "5m": "60d"}
            df = yf.Ticker(symbol)
            df = df.history(period=period_map[timeframe], interval=timeframe)
            df = df.rename(columns={
                f'Close': 'close',
                f'High': 'high',
                f'Low': 'low',
                f'Open': 'open',
                f'Volume': 'volume',
                f'Dividends': 'dividends',
                f'Stock Splits': 'stock splits'
            })
            df.index.rename('datetime', inplace=True)
            # filename = 'data_with_indicators/%s-%s-data.csv' % (symbol, timeframe)
            # df.set_index('datetime', inplace=True)
            df.to_csv(f'{filename}', index=True, sep=";")
    return filename


def get_tradovate_data(symbol, timeframe="1m"):
    filename = 'data_with_indicators/%s-%s-%s-%s-data.csv' % (
        symbol, timeframe, definitions.HISTORICAL_DATA_FROM, definitions.HISTORICAL_DATA_TO
    )
    if os.path.isfile(filename):
        data_df = pd.read_csv(filename)
    else:
        db = DB().connection
        db_cursor = db.cursor(dictionary=True)
        db_cursor.execute(
            "select * from minute_bars where `symbol` = %s and `timestamp` between %s and %s order by `timestamp` asc;",
            [
                definitions.SYMBOL,
                definitions.START_DATE,
                definitions.END_DATE
            ]
        )
        result = db_cursor.fetchall()
        filename = 'data_with_indicators/%s-%s-%s-%s-data.csv' % (
            symbol, timeframe, definitions.HISTORICAL_DATA_FROM, definitions.HISTORICAL_DATA_TO
        )
        df = pd.DataFrame(result)
        df.rename(columns={'timestamp': 'datetime'}, inplace=True)
        df.drop(df.columns[[0]], axis=1, inplace=True)
        df.to_csv(f'{filename}', index=True, sep=";")
        # print(result)
    return filename


