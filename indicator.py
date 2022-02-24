#!/usr/bin/python
# -*- encoding: utf-8 -*-

__author__ = 'Jan Olschewski, Ingo Volkmann'
import pandas as pd


def last_5_10_15_20_candles(df, filename):
    if df.get('largest_body_5') is not None \
            and df.get('largest_body_10') is not None \
            and df.get('largest_body_15') is not None \
            and df.get('largest_body_20') is not None:
        return df

    print('Writing last_5_10_15_20_candles to dataframe')

    data = {}
    missing = list()

    if df.get('largest_body_5') is None:
        print('last 5 candles missing')
        missing.append(5)
        data.update({
            'highest_high_5': list(),
            'lowest_low_5': list(),
            'largest_body_5': list(),
        })
    if df.get('largest_body_10') is None:
        print('last 10 candles missing')
        missing.append(10)
        data.update({
            'highest_high_10': list(),
            'lowest_low_10': list(),
            'largest_body_10': list(),
        })
    if df.get('largest_body_15') is None:
        print('last 15 candles missing')
        missing.append(15)
        data.update({
            'highest_high_15': list(),
            'lowest_low_15': list(),
            'largest_body_15': list(),
        })
    if df.get('largest_body_20') is None:
        print('last 20 candles missing')
        missing.append(20)
        data.update({
            'highest_high_20': list(),
            'lowest_low_20': list(),
            'largest_body_20': list(),
        })

    # data = {
    #     'highest_high_5': list(),
    #     'lowest_low_5': list(),
    #     'largest_body_5': list(),
    #     'highest_high_10': list(),
    #     'lowest_low_10': list(),
    #     'largest_body_10': list(),
    #     'highest_high_15': list(),
    #     'lowest_low_15': list(),
    #     'largest_body_15': list(),
    #     'highest_high_20': list(),
    #     'lowest_low_20': list(),
    #     'largest_body_20': list(),
    # }

    def build_data(list_of_latest, number_of_candles):
        # get largest candle of the last n candles
        largest_body = None if list_of_latest is None else 0
        # find the highest high of the last n candles
        highest_high = None if list_of_latest is None else 0
        # find lowest low of the last n candles
        lowest_low = None if list_of_latest is None else 0

        if list_of_latest is not None:
            for row in list_of_latest:
                # largest candle
                diff = abs(row['close'] - row['open'])
                if diff > largest_body:
                    largest_body = diff
                # highest high
                if row['high'] > highest_high:
                    highest_high = row['high']
                # lowest low
                if lowest_low == 0 or row['low'] < lowest_low:
                    lowest_low = row['low']

        data[f'highest_high_{number_of_candles}'].append(highest_high)
        data[f'lowest_low_{number_of_candles}'].append(lowest_low)
        data[f'largest_body_{number_of_candles}'].append(largest_body)

    last5 = list()
    last10 = list()
    last15 = list()
    last20 = list()
    for (line, (index, row)) in enumerate(df.iterrows()):

        if 5 in missing:
            if line >= 5:
                build_data(last5, 5)
                last5.pop(0)
            else:
                build_data(None, 5)

        if 10 in missing:
            if line >= 10:
                build_data(last10, 10)
                last10.pop(0)
            else:
                build_data(None, 10)

        if 15 in missing:
            if line >= 15:
                build_data(last15, 15)
                last15.pop(0)
            else:
                build_data(None, 15)

        if 20 in missing:
            if line >= 20:
                build_data(last20, 20)
                last20.pop(0)
            else:
                build_data(None, 20)

        last5.append(row)
        last10.append(row)
        last15.append(row)
        last20.append(row)

    data_df = pd.DataFrame(data, index=df.index)
    df = pd.concat([df, data_df], axis=1, join='inner')
    df.to_csv(filename, index=True, sep=";")

    print('done')

    return df
