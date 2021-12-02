#!/usr/bin/python
# -*- encoding: utf-8 -*-

__author__ = 'Olschewski, Jan'
from definitions import INDICATORS
import pandas_ta as ta

# INDICATORS AT: https://github.com/voice32/stock_market_indicators/blob/master/indicators.py

def exponential_moving_average(df, window):
    df_name = f'{window} Day EMA'
    df[df_name] = df['Close'].ewm(span=window, adjust=False).mean()

    INDICATORS.append(df_name)
    return df

def adx_indicator(data, window=14):
    data_new = data.ta.adx()

    data_new = data_new.rename(columns={f'ADX_{window}': 'ADX', f'DMP_{window}': 'DMP', f'DMN_{window}': 'DMN'})
    data = data.join(data_new)
    INDICATORS.extend(['ADX', 'DMP', 'DMN'])
    return data
