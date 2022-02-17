#!/usr/bin/python
# -*- encoding: utf-8 -*-

import mplfinance as mpf
from definitions import INDICATORS

def plot_data(df):
    additional_plots = list()
    INDICATORS = ['ADX', 'DMP', 'DMN', f'{8} Day EMA', f'{13} Day EMA']

    # for indicator in INDICATORS:
    #     if indicator == 'ADX':
    #         additional_plots.append(mpf.make_addplot(df[indicator], color='grey', panel='lower'))
    #     elif indicator == 'DMP':
    #         additional_plots.append(mpf.make_addplot(df[indicator], color='green', panel='lower', linestyle="dotted"))
    #     elif indicator == 'DMN':
    #         additional_plots.append(mpf.make_addplot(df[indicator], color='red', panel='lower', linestyle="dotted"))
    #     else:
    #         additional_plots.append(mpf.make_addplot(df[indicator]))

    if 'create_order' in df:
        additional_plots.append(mpf.make_addplot(df['create_order'], scatter=True, markersize=200, marker='^', color='#777777'))
    if 'close_order' in df:
        additional_plots.append(mpf.make_addplot(df['close_order'], scatter=True, markersize=200, marker='v', color="#a00000"))
    # if 'close_order_l' in df:
    #     additional_plots.append(mpf.make_addplot(df['close_order_l'], scatter=True, markersize=200, marker='v', color='#128000'))
    # if 'close_order_l2' in df:
    #     additional_plots.append(mpf.make_addplot(df['close_order_l2'], scatter=True, markersize=200, marker='v',  color='#1dcc00'))
    # if 'current gains' in df:
    #     additional_plots.append(mpf.make_addplot((df['current gains']), panel='lower', color='yellow', linestyle="dashdot", secondary_y=True))

    mpf.plot(df, type="candle", style='charles', addplot=additional_plots, figsize=(50, 50))



