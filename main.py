import strategy
import dataframe
import plot
import indicator
from api import get_all_binance
from portfolio import Portfolio
from definitions import *
from datetime import date

sdate = date(2018, 4, 1)   # start date
edate = date(2020, 4, 1)
TIMEFRAME = "4h"
SYMBOL = 'BTCUSDT'


def frange(start,stop, step=1.0):
    while start < stop:
        yield start
        start +=step


def main():
    NUMBER_OF_TESTS = 0
    OVR = 0
    get_all_binance(SYMBOL, TIMEFRAME)
    df = prepare_df(SYMBOL)

    for limit in frange(102.5, 105.0, 0.5):
        for stop in frange(98.0, 100.0, 0.5):
            NUMBER_OF_TESTS += 1
            OVR += test_single_symbol(df, stop, limit, False)

    print(f'AVG Performance: {OVR / NUMBER_OF_TESTS}')


def test(df, pf , stop, limit):
    df, pf = strategy.ma_crossing_adx(df, pf, 8, 13, stop, limit)
    performance = round((pf.cash / STARTING_AMOUNT * 100) - 100, 4)

    if performance > 5: # and pf.positive > pf.negative:
        print(f'Performance: {performance} % - Stop:{stop}, Limit {limit} - {pf.positive/pf.negative}') # - positive: {pf.positive}, negative: {pf.negative}' )

    return performance
    # print(f"Starting cash: \t\t\t {STARTING_AMOUNT}")
    # print(f"Ending cash: \t\t\t {round(pf.cash, 2)}")
    # print(f"Chart performance: \t\t {round((df['Close'].iloc[-1] - df['Close'].iloc[1]) / df['Close'].iloc[1] *100, 4)} %")
    # print(f'Algorithm performance: \t {round((pf.cash/ STARTING_AMOUNT *100) - 100, 4)} %')
    # print(f'positive: {pf.positive}, negative: {pf.negative}')


def prepare_df(item):
    df = dataframe.trading_data_from_csv(item, time=TIMEFRAME, add_indicators=False)
    df = df.loc[f'{sdate} 00:00:00-00:00':f'{edate} 23:00:00-00:00']

    df = indicator.exponential_moving_average(df, 8)
    df = indicator.exponential_moving_average(df, 13)
    df = indicator.adx_indicator(df)

    df = df.rename(columns={f'close': 'Close', f'high': 'High', f'low': 'Low', f'open': 'Open'})
    return df


def test_single_symbol(df, stop, limit, chart=False):
    pf = Portfolio(STARTING_AMOUNT)

    performance = test(df, pf, stop, limit)
    pf.close_all_orders(df, df['Close'].iloc[-1])

    if chart:
        plot.plot_data(df)

    return performance


def live_trading():
    # check system status
    # check account balance
    # if account balance high trade
    # check symbol data
    # calculate mfi for timestamp
    pass


main()

