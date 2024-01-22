#!/usr/bin/python
# -*- encoding: utf-8 -*-

__author__ = 'Jan Olschewski, Ingo Volkmann'
import pandas as pd

import definitions


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


def aroon(df, filename, period):
    name = 'aroon_' + str(period)
    if df.get(f'{name}_up') is not None and df.get(f'{name}_down') is not None:
        return df

    print(f'Writing {name} to dataframe')

    data = {}
    missing = list()
    missing.append(2)
    data.update({
        name: list(),
    })

    def aroon_indicator(_df, _period):
        _aroon_up = (_df['high'].rolling(window=_period).apply(lambda x: x.argmax(), raw=True) / (_period - 1)) * 100
        _aroon_down = (_df['low'].rolling(window=_period).apply(lambda x: x.argmin(), raw=True) / (_period - 1)) * 100

        return _aroon_up, _aroon_down

    aroon_up, aroon_down = aroon_indicator(df, period)
    df[f'{name}_up'] = aroon_up
    df[f'{name}_down'] = aroon_down
    df.to_csv(filename, index=True, sep=";")

    print('done')

    return df


def ma_cross(df, filename, fast_period, slow_period):
    name_fast = 'ma_' + str(fast_period)
    name_slow = 'ma_' + str(slow_period)
    # golden cross - fast ma crosses the slow one from down to up
    name_golden_cross = 'ma_golden_cross_' + str(fast_period) + '_' + str(slow_period)
    # death cross - slow ma crosses the fast one from down to up
    name_death_cross = 'ma_death_cross_' + str(fast_period) + '_' + str(slow_period)
    if df.get(f'{name_fast}') is not None \
            and df.get(f'{name_slow}') is not None \
            and df.get(f'{name_golden_cross}') is not None \
            and df.get(f'{name_death_cross}') is not None:
        return df

    print(f'Writing {name_fast}, {name_slow} and ma_cross of both to dataframe')

    df[name_fast] = df['close'].rolling(window=fast_period).mean()
    df[name_slow] = df['close'].rolling(window=slow_period).mean()
    df[name_golden_cross] = (df[name_fast] > df[name_slow]) & (df[name_fast].shift(1) <= df[name_slow].shift(1))
    df[name_death_cross] = (df[name_fast] < df[name_slow]) & (df[name_fast].shift(1) >= df[name_slow].shift(1))

    df.to_csv(filename, index=True, sep=";")

    print('done')

    return df


def fractals(df, filename, period):
    if period < 5:
        raise ValueError("Period must be at least 5.")

    # fractals will be calculated at the end of `period` bars for the middle of the period
    # but the signal will be added to the current candle and indicates, that a Fractal occurred
    name_bullish = f'fractal_{period}_bullish'
    name_bearish = f'fractal_{period}_bearish'
    moving = period // 2

    if df.get(f'{name_bullish}') is not None \
            and df.get(f'{name_bearish}') is not None:
        return df

    print(f'Writing fractal_{period} to dataframe')

    df[name_bullish] = False
    for i in range(moving, len(df) - moving):
        if df['high'][i] == max(df['high'][i - moving:i + moving + 1]):
            df.at[i, name_bullish] = True

    df[name_bearish] = False
    for i in range(moving, len(df) - moving):
        if df['low'][i] == min(df['low'][i - moving:i + moving + 1]):
            df.at[i, name_bearish] = True

    df.to_csv(filename, index=True, sep=";")

    print('done')

    return df


def fractals(df, filename, period):
    # fractals will be calculated at the end of `period` bars for the middle of the period
    # but the signal will be added to the current candle - that means, a fractal occurs right before
    name_bullish = f'fractal_{period}_bullish'
    name_bearish = f'fractal_{period}_bearish'

    df[name_bullish] = ((df['high'].shift(2) < df['high'].shift(3)) &
                             (df['high'].shift(1) < df['high'].shift(3)) &
                             (df['high'].shift(3) > df['high'].shift(4)) &
                             (df['high'].shift(3) > df['high'].shift(5))).shift(-2)

    df[name_bearish] = ((df['low'].shift(2) > df['low'].shift(3)) &
                             (df['low'].shift(1) > df['low'].shift(3)) &
                             (df['low'].shift(3) < df['low'].shift(4)) &
                             (df['low'].shift(3) < df['low'].shift(5))).shift(-2)

    return df
