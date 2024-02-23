#!/usr/bin/python
# -*- encoding: utf-8 -*-

__author__ = 'Ingo Volkmann'
import pandas as pd

import definitions

'''
*** MOMENTUM + TREND
*** Diese Indikatoren helfen dabei, die Stärke eines Trends zu beurteilen und die Richtung des Markttrends zu 
    identifizieren.

MACD (Moving Average Convergence Divergence)
    Zeigt die Beziehung zwischen zwei gleitenden Durchschnitten des Preises.
Ichimoku Cloud
    Ein umfassender Trendindikator, der auch Aspekte von Support/Resistance, Momentum und Trendrichtung abdeckt und für 
    die Trendvisualisierung sowie die Identifizierung von Handelssignalen verwendet wird.

*** TREND
*** Diese Indikatoren helfen dabei, die Richtung des Markttrends zu identifizieren.

AROON
    Misst die Zeit zwischen Höchst- und Tiefstwerten über einen bestimmten Zeitraum.
Moving Averages (MA)
    Glättet Preisdaten, um den Trendverlauf zu identifizieren.
Parabolic SAR
    Bestimmt den Trendverlauf und potenzielle Umkehrpunkte.
EMA (Exponential Moving Average)
    Eine Art von gleitendem Durchschnitt, der den neuesten Daten mehr Gewicht verleiht.
Vortex Indicator
    Identifiziert den Beginn eines neuen Trends oder die Bestätigung eines aktuellen Trends.
Hull Moving Average
    Bietet eine schnellere und glattere Version des traditionellen gleitenden Durchschnitts.
Keltner Channels
    Bestimmt Trendrichtung und Volatilität mit einem zentralen gleitenden Durchschnitt und äußeren Kanälen.
Fibonacci Retracements
    Identifiziert Unterstützungs- und Widerstandsniveaus in einem Trend.

*** VOLUMEN
*** Diese Indikatoren verwenden Volumendaten, um die Stärke eines Trends oder einer Marktbewegung zu bewerten.

Volume SMA (Simple Moving Average of Volume)
    Glättet das Handelsvolumen, um Trends zu erkennen.
Elders Force Index
    Kombiniert Preis- und Volumendaten, um die Kraft hinter einer Preisbewegung zu messen.
Chaikin Volatility
    Misst die Volatilität des Marktes durch die Untersuchung des Volumens und der Preisspanne.
Accumulation/Distribution Line (ADL)
    Misst den Geldfluss und weist auf Akkumulations- oder Verteilungsphasen eines Wertpapiers hin.

*** OSZILLATOREN
*** Diese Indikatoren schwanken in der Regel innerhalb eines bestimmten Bereichs und helfen, überkaufte oder 
    überverkaufte Bedingungen zu identifizieren.

Williams %R
    Misst das Verhältnis von Schlusskurs zu Hoch/Tief über einen bestimmten Zeitraum, um überkaufte/überverkaufte 
    Zustände zu identifizieren.
RSI (Relative Strength Index)
    Misst die Stärke und Geschwindigkeit von Preisbewegungen.
DeMarker Indicator
    Misst die Nachfrage des zugrundeliegenden Vermögenswerts, indem die Höchst- und Tiefstwerte der aktuellen Periode 
    analysiert werden.

*** VOLATILITÄT
*** Diese Indikatoren messen die Rate der Preisänderungen, unabhängig von der Richtung.

Bollinger Bands
    Nutzt eine Standardabweichung des Preises, um die Marktvolatilität zu messen.
Average True Range (ATR)
    Misst die Marktvotalität durch die Analyse des gesamten Preisbereichs.
Historical Volatility
    Misst die Schwankungen der Preisänderungen über einen bestimmten Zeitraum.

*** MUSTER
*** Diese Indikatoren identifizieren spezifische Preisformationen oder Muster.

Fractals
    Identifiziert Muster im Preisverlauf, die auf Wendepunkte im Markttrend hinweisen können.
'''

def get_example_df():
    data = {
        'open': [0.8, 1.8, 2.9, 3.6, 4.5],
        'high': [1, 2, 3, 4, 5],
        'low': [0.5, 1.5, 2.5, 3.5, 4.5],
        'close': [0.75, 1.75, 2.75, 3.75, 4.75]
    }
    return pd.DataFrame(data)


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

    def build_data(list_of_latest, number_of_candles):
        # get largest candle of the last n candles
        largest_body = None if list_of_latest is None else 0
        # find the highest high of the last n candles
        highest_high = None if list_of_latest is None else 0
        # find lowest low of the last n candles
        lowest_low = None if list_of_latest is None else 0

        if list_of_latest is not None:
            for row_latest in list_of_latest:
                # largest candle
                diff = abs(row_latest['close'] - row_latest['open'])
                if diff > largest_body:
                    largest_body = diff
                    if largest_body is not None:
                        largest_body = round(largest_body, 4)
                # highest high
                if row_latest['high'] > highest_high:
                    highest_high = row_latest['high']
                    if highest_high is not None:
                        highest_high = round(highest_high, 4)
                # lowest low
                if lowest_low == 0 or row_latest['low'] < lowest_low:
                    lowest_low = row_latest['low']
                    if lowest_low is not None:
                        lowest_low = round(lowest_low, 4)

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


def last_30_40_50_75_100_candles(df, filename):
    if df.get('largest_body_30') is not None \
            and df.get('largest_body_40') is not None \
            and df.get('largest_body_50') is not None \
            and df.get('largest_body_75') is not None \
            and df.get('largest_body_100') is not None:
        return df

    print('Writing last_30_40_50_75_100_candles to dataframe')

    data = {}
    missing = list()

    if df.get('largest_body_30') is None:
        print('last 30 candles missing')
        missing.append(30)
        data.update({
            'highest_high_30': list(),
            'lowest_low_30': list(),
            'largest_body_30': list(),
        })
    if df.get('largest_body_40') is None:
        print('last 40 candles missing')
        missing.append(40)
        data.update({
            'highest_high_40': list(),
            'lowest_low_40': list(),
            'largest_body_40': list(),
        })
    if df.get('largest_body_50') is None:
        print('last 50 candles missing')
        missing.append(50)
        data.update({
            'highest_high_50': list(),
            'lowest_low_50': list(),
            'largest_body_50': list(),
        })
    if df.get('largest_body_75') is None:
        print('last 75 candles missing')
        missing.append(75)
        data.update({
            'highest_high_75': list(),
            'lowest_low_75': list(),
            'largest_body_75': list(),
        })
    if df.get('largest_body_100') is None:
        print('last 100 candles missing')
        missing.append(100)
        data.update({
            'highest_high_100': list(),
            'lowest_low_100': list(),
            'largest_body_100': list(),
        })

    def build_data(list_of_latest, number_of_candles):
        # get largest candle of the last n candles
        largest_body = None if list_of_latest is None else 0
        # find the highest high of the last n candles
        highest_high = None if list_of_latest is None else 0
        # find lowest low of the last n candles
        lowest_low = None if list_of_latest is None else 0

        if list_of_latest is not None:
            for row_latest in list_of_latest:
                # largest candle
                diff = abs(row_latest['close'] - row_latest['open'])
                if diff > largest_body:
                    largest_body = diff
                    if largest_body is not None:
                        largest_body = round(largest_body, 4)
                # highest high
                if row_latest['high'] > highest_high:
                    highest_high = row_latest['high']
                    if highest_high is not None:
                        highest_high = round(highest_high, 4)
                # lowest low
                if lowest_low == 0 or row_latest['low'] < lowest_low:
                    lowest_low = row_latest['low']
                    if lowest_low is not None:
                        lowest_low = round(lowest_low, 4)

        data[f'highest_high_{number_of_candles}'].append(highest_high)
        data[f'lowest_low_{number_of_candles}'].append(lowest_low)
        data[f'largest_body_{number_of_candles}'].append(largest_body)

    last30 = list()
    last40 = list()
    last50 = list()
    last75 = list()
    last100 = list()
    for (line, (index, row)) in enumerate(df.iterrows()):
        if 30 in missing:
            if line >= 30:
                build_data(last30, 30)
                last30.pop(0)
            else:
                build_data(None, 30)

        if 40 in missing:
            if line >= 40:
                build_data(last40, 40)
                last40.pop(0)
            else:
                build_data(None, 40)

        if 50 in missing:
            if line >= 50:
                build_data(last50, 50)
                last50.pop(0)
            else:
                build_data(None, 50)

        if 75 in missing:
            if line >= 75:
                build_data(last75, 75)
                last75.pop(0)
            else:
                build_data(None, 75)

        if 100 in missing:
            if line >= 100:
                build_data(last100, 100)
                last100.pop(0)
            else:
                build_data(None, 100)

        last30.append(row)
        last40.append(row)
        last50.append(row)
        last75.append(row)
        last100.append(row)

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

        return round(_aroon_up, 4), round(_aroon_down, 4)

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

    df[name_fast] = df['close'].rolling(window=fast_period).mean().round(4)
    df[name_slow] = df['close'].rolling(window=slow_period).mean().round(4)
    df[name_golden_cross] = (df[name_fast] > df[name_slow]) & (df[name_fast].shift(1) <= df[name_slow].shift(1))
    df[name_death_cross] = (df[name_fast] < df[name_slow]) & (df[name_fast].shift(1) >= df[name_slow].shift(1))

    df.to_csv(filename, index=True, sep=";")

    print('done')

    return df


def fractals(df, filename, period):
    # fractals will be calculated at the end of `period` bars for the middle of the period
    # but the signal will be added to the current candle - that means, a fractal occurs right before
    name_bullish = f'fractal_{period}_bullish'
    name_bearish = f'fractal_{period}_bearish'

    if df.get(f'{name_bullish}') is not None \
            and df.get(f'{name_bearish}') is not None:
        return df

    print(f'Writing fractal_{period} to dataframe')

    df[name_bullish] = ((df['high'].shift(2) < df['high'].shift(3)) &
                             (df['high'].shift(1) < df['high'].shift(3)) &
                             (df['high'].shift(3) > df['high'].shift(4)) &
                             (df['high'].shift(3) > df['high'].shift(5))).shift(-2)

    df[name_bearish] = ((df['low'].shift(2) > df['low'].shift(3)) &
                             (df['low'].shift(1) > df['low'].shift(3)) &
                             (df['low'].shift(3) < df['low'].shift(4)) &
                             (df['low'].shift(3) < df['low'].shift(5))).shift(-2)

    df.loc[df.index[-2:], [name_bullish, name_bearish]] = False

    df.to_csv(filename, index=True, sep=";")

    print('done')

    return df


def parabolic_sar(df, filename, acceleration_factor=0.02, max_acceleration_factor=0.2):
    # die künftigen Spaltennamen holen um zu prüfen, ob sie bereits im DF vorhanden sind
    column_names = get_example_df().ta.psar(af=acceleration_factor,
                                            max_af=max_acceleration_factor, append=False).columns

    if not all(col in df.columns for col in column_names):
        print(f'Writing {", ".join(column_names)} to dataframe')
        df.ta.psar(af=acceleration_factor, max_af=max_acceleration_factor, append=True)
        df.to_csv(filename, index=True, sep=";")
        print('done')

    return df


def volume_sma(df, filename, period=9):
    name_sma = f'volume_sma_{period}'
    if name_sma not in df.columns:
        print(f'Writing {name_sma} to dataframe')
        df[name_sma] = df['volume'].rolling(window=period).mean()
        df.to_csv(filename, index=True, sep=";")
        print('done')
    return df


def williams_r(df, filename, period=14):
    name_wr = f'williams_r_{period}'
    if name_wr not in df.columns:
        print(f'Writing {name_wr} to dataframe')
        df[name_wr] = ((df['high'].rolling(window=period).max() - df['close']) /
                       (df['high'].rolling(window=period).max() - df['low'].rolling(window=period).min())) * -100
        df.to_csv(filename, index=True, sep=";")
        print('done')
    return df


def vortex_indicator(df, filename, period=14):
    name_vi = f'vortex_{period}'
    if f'{name_vi}_pos' not in df.columns and f'{name_vi}_neg' not in df.columns:
        print(f'Writing {name_vi} to dataframe')
        df['tr'] = abs(df['high'] - df['low'])
        df['vm_plus'] = abs(df['high'] - df['low'].shift(1))
        df['vm_minus'] = abs(df['low'] - df['high'].shift(1))
        df['tr_n'] = df['tr'].rolling(window=period).sum()
        df['vm_plus_n'] = df['vm_plus'].rolling(window=period).sum()
        df['vm_minus_n'] = df['vm_minus'].rolling(window=period).sum()
        df[f'{name_vi}_pos'] = df['vm_plus_n'] / df['tr_n']
        df[f'{name_vi}_neg'] = df['vm_minus_n'] / df['tr_n']
        df.drop(['tr', 'vm_plus', 'vm_minus', 'tr_n', 'vm_plus_n', 'vm_minus_n'], axis=1, inplace=True)
        df.to_csv(filename, index=True, sep=";")
        print('done')
    return df


def ema(df, filename, period=100):
    name_ema = f'ema_{period}'
    if name_ema not in df.columns:
        print(f'Writing {name_ema} to dataframe')
        df[name_ema] = df['close'].ewm(span=period, adjust=False).mean()
        df.to_csv(filename, index=True, sep=";")
        print('done')
    return df


def accumulation_distribution(df, filename):
    name_ad = 'accumulation_distribution'
    if name_ad not in df.columns:
        print(f'Writing {name_ad} to dataframe')
        df[name_ad] = ((df['close'] - df['low']) - (df['high'] - df['close'])) / (df['high'] - df['low']) * df['volume']
        df[name_ad] = df[name_ad].cumsum()
        df.to_csv(filename, index=True, sep=";")
        print('done')
    return df


def chaikin_volatility(df, filename, ema_period=10, change_period=10):
    name_cv = f'chaikin_volatility_{ema_period}_{change_period}'
    if name_cv not in df.columns:
        print(f'Writing {name_cv} to dataframe')
        df['high_low_range'] = df['high'] - df['low']
        df['ema_hl_range'] = df['high_low_range'].ewm(span=ema_period, adjust=False).mean()
        df[name_cv] = df['ema_hl_range'].pct_change(periods=change_period) * 100
        df.drop(['high_low_range', 'ema_hl_range'], axis=1, inplace=True)
        df.to_csv(filename, index=True, sep=";")
        print('done')
    return df


def macd(df, filename, short_period=12, long_period=26, signal_period=9):
    name_macd = f'macd_{short_period}_{long_period}_signal_{signal_period}'
    if f'{name_macd}_line' not in df.columns and f'{name_macd}_signal' not in df.columns:
        print(f'Writing {name_macd} to dataframe')
        df['ema_short'] = df['close'].ewm(span=short_period, adjust=False).mean()
        df['ema_long'] = df['close'].ewm(span=long_period, adjust=False).mean()
        df[f'{name_macd}_line'] = df['ema_short'] - df['ema_long']
        df[f'{name_macd}_signal'] = df[f'{name_macd}_line'].ewm(span=signal_period, adjust=False).mean()
        df.drop(['ema_short', 'ema_long'], axis=1, inplace=True)
        df.to_csv(filename, index=True, sep=";")
        print('done')
    return df


def historical_volatility(df, filename, period=10):
    name_hv = f'historical_volatility_{period}'
    if name_hv not in df.columns:
        print(f'Writing {name_hv} to dataframe')
        df[name_hv] = df['close'].pct_change().rolling(window=period).std() * (252**0.5)  # Annualized Volatility
        df.to_csv(filename, index=True, sep=";")
        print('done')
    return df


def rsi(df, filename, period=14):
    name_rsi = f'rsi_{period}'
    if name_rsi not in df.columns:
        print(f'Writing {name_rsi} to dataframe')
        delta = df['close'].diff(1)
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        df[name_rsi] = 100 - (100 / (1 + rs))
        df.to_csv(filename, index=True, sep=";")
        print('done')
    return df


def bollinger_bands(df, filename, period=20, num_std=2):
    name_sma = f'sma_{period}'
    name_prefix = f'bollinger_bands_{period}_{num_std}'
    name_upper = f'{name_prefix}_upper'
    name_lower = f'{name_prefix}_lower'

    # Überprüfen, ob die SMA-Spalte bereits existiert. Wenn nicht, wird sie berechnet.
    if name_sma not in df.columns:
        df[name_sma] = df['close'].rolling(window=period).mean()

    if df.get(name_sma) is not None and df.get(name_upper) is not None and df.get(name_lower) is not None:
        return df

    print(f'Writing {name_prefix} to dataframe')
    std = df['close'].rolling(window=period).std()
    df[name_upper] = df[name_sma] + (std * num_std)
    df[name_lower] = df[name_sma] - (std * num_std)

    df.to_csv(filename, index=True, sep=";")
    print('done')
    return df


def ichimoku_cloud(df, filename):
    cols = ['ichimoku_conversion', 'ichimoku_base', 'ichimoku_leading_a', 'ichimoku_leading_b', 'ichimoku_lagging']
    if not all(col in df.columns for col in cols):
        print(f'Writing Ichimoku Cloud components to dataframe')
        high_9 = df['high'].rolling(window=9).max()
        low_9 = df['low'].rolling(window=9).min()
        df['ichimoku_conversion'] = (high_9 + low_9) / 2

        high_26 = df['high'].rolling(window=26).max()
        low_26 = df['low'].rolling(window=26).min()
        df['ichimoku_base'] = (high_26 + low_26) / 2

        df['ichimoku_leading_a'] = ((df['ichimoku_conversion'] + df['ichimoku_base']) / 2).shift(26)
        df['ichimoku_leading_b'] = (
                    (df['high'].rolling(window=52).max() + df['low'].rolling(window=52).min()) / 2).shift(26)

        df['ichimoku_lagging'] = df['close'].shift(-26)

        df.to_csv(filename, index=True, sep=";")
        print('done')
    return df


def hma(df, filename, period=9):
    name_hma = f'hma_{period}'
    if name_hma not in df.columns:
        print(f'Writing {name_hma} to dataframe')
        wma_half_period = df['close'].rolling(window=int(period / 2)).mean()
        wma_full_period = df['close'].rolling(window=period).mean()
        raw_hma = 2 * wma_half_period - wma_full_period
        df[name_hma] = raw_hma.rolling(window=int(period ** 0.5)).mean()

        df.to_csv(filename, index=True, sep=";")
        print('done')
    return df


def elders_force_index(df, filename, period=13):
    name_efi = f'efi_{period}'
    if name_efi not in df.columns:
        print(f'Writing {name_efi} to dataframe')
        df[name_efi] = (df['close'] - df['close'].shift(1)) * df['volume']
        df[name_efi] = df[name_efi].ewm(span=period, adjust=False).mean()

        df.to_csv(filename, index=True, sep=";")
        print('done')
    return df


def demarker_indicator(df, filename, period=14):
    name_dem = f'dem_{period}'
    if name_dem not in df.columns:
        print(f'Writing {name_dem} to dataframe')
        de_max = df['high'].diff(1).apply(lambda x: x if x > 0 else 0).rolling(window=period).sum()
        de_min = df['low'].diff(1).apply(lambda x: x if x < 0 else 0).rolling(window=period).sum().abs()
        df[name_dem] = de_max / (de_max + de_min)

        df.to_csv(filename, index=True, sep=";")
        print('done')
    return df


def fibonacci_retracements(df, filename, period=100):
    fib_name = f'fib_{period}'
    cols = [f'{fib_name}_23.6', f'{fib_name}_38.2', f'{fib_name}_50.0', f'{fib_name}_61.8', f'{fib_name}_78.6']
    if not all(col in df.columns for col in cols):
        print(f'Writing {fib_name} to dataframe')
        # Berechnung der signifikanten Hoch- und Tiefpunkte innerhalb des gewählten Zeitraums
        period_high = df['high'].rolling(window=period).max()
        period_low = df['low'].rolling(window=period).min()

        # Berechnung der Fibonacci-Retracement-Level basierend auf den signifikanten Hoch- und Tiefpunkten
        diff = period_high - period_low
        df[f'{fib_name}_23.6'] = period_high - diff * 0.236
        df[f'{fib_name}_38.2'] = period_high - diff * 0.382
        df[f'{fib_name}_50.0'] = period_high - diff * 0.5
        df[f'{fib_name}_61.8'] = period_high - diff * 0.618
        df[f'{fib_name}_78.6'] = period_high - diff * 0.786

        # Speichern der Ergebnisse
        df.to_csv(filename, index=True, sep=";")

        print('done')
    return df


def keltner_channels(df, filename, ema_period=20, atr_period=10, multiplier=2):
    # Namensgebung für die Spalten basierend auf den übergebenen Parametern
    name_ema = f'ema_{ema_period}'
    name_upper = f'keltner_{ema_period}_{atr_period}_{multiplier}_upper'
    name_lower = f'keltner_{ema_period}_{atr_period}_{multiplier}_lower'

    # Überprüfen, ob die EMA-Spalte bereits existiert. Wenn nicht, wird sie berechnet.
    if name_ema not in df.columns:
        df[name_ema] = df['close'].ewm(span=ema_period, adjust=False).mean()

    if df.get(name_ema) is not None and df.get(name_upper) is not None and df.get(name_lower) is not None:
        return df

    print(f'Writing keltner_channels_{ema_period}_{atr_period}_{multiplier} to dataframe')

    # Berechnung des Average True Range (ATR)
    df['tr0'] = abs(df['high'] - df['low'])
    df['tr1'] = abs(df['high'] - df['close'].shift())
    df['tr2'] = abs(df['low'] - df['close'].shift())
    df['tr'] = df[['tr0', 'tr1', 'tr2']].max(axis=1)
    df['atr'] = df['tr'].rolling(window=atr_period).mean()

    # Berechnung der oberen und unteren Keltner Channel Linien
    df[name_upper] = df[name_ema] + (df['atr'] * multiplier)
    df[name_lower] = df[name_ema] - (df['atr'] * multiplier)

    # Entfernen der temporären Spalten
    df.drop(['tr0', 'tr1', 'tr2', 'tr', 'atr'], axis=1, inplace=True)
    # Optional: Speichern der Ergebnisse
    df.to_csv(filename, index=True, sep=";")
    print('done')

    return df


def average_true_range(df, filename, period=20):
    # Namensgebung für die Spalten basierend auf den übergebenen Parametern
    name_atr = f'atr_{period}'

    if df.get(name_atr) is not None:
        return df

    print(f'Writing {name_atr} to dataframe')

    # Berechnung der einzelnen True Ranges
    df['high_low'] = df['high'] - df['low']
    df['high_close_prev'] = abs(df['high'] - df['close'].shift())
    df['low_close_prev'] = abs(df['low'] - df['close'].shift())
    # Auswahl des maximalen True Range Wertes für jede Zeile
    df['tr'] = df[['high_low', 'high_close_prev', 'low_close_prev']].max(axis=1)
    # Berechnung des ATR
    df[name_atr] = df['tr'].rolling(window=period).mean()

    # Optional: Entfernen der temporären Spalten
    df.drop(['high_low', 'high_close_prev', 'low_close_prev', 'tr'], axis=1, inplace=True)
    df.to_csv(filename, index=True, sep=";")
    print('done')

    return df
