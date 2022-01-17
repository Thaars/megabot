import multiprocessing

from regex import R

import strategy
import dataframe
import plot
import indicator
from api import get_all_binance, get_stock_data
from portfolio import Portfolio
from definitions import *
from datetime import date

# sdate = date(2018, 4, 1)  # start date
# edate = date(2020, 4, 1)


sdate = date(2018, 4, 1)  # start date
edate = date(2020, 4, 1) # edate = date(2018, 8, 15)
TIMEFRAME = "1h"
SYMBOL = 'BTCUSDT'
EMA_LENGTH = 20


def frange(start, stop, step=1.0):
    while start <= stop:
        yield start
        start += step


def worker(limit):
    print(f'Worker spawned')
    start_emas(limit)
    print(f"Worker finished the work")


def start_emas():
    workers = []

    test_single_symbol(SYMBOL, 98, 103, 9, 13, True)
    return
    for limit in frange(102, 106.5, 0.5):
        for stop in frange(97, 99, 0.5):
            for ema_short in range(3, EMA_LENGTH + 1):
                for ema_long in range(3, EMA_LENGTH + 1):
                    if ema_short < ema_long - 2 and 100 - stop <= limit - 100:
                        test_single_symbol(SYMBOL, stop, limit, ema_short, ema_long, False)
                        #
                        # # while True:
                        # #     if len(worker) <= 4:
                        # w = multiprocessing.Process(
                        #     target=worker,
                        #     args=(stop, limit, ema_short, ema_long)
                        # )
                        # workers.append(w)
                        #
                        # for w in workers:
                        #     w.start()
                        #
                        # for w in workers:
                        #     w.join()
                        #
                        #         # break


def main():
    # get_all_binance(SYMBOL, TIMEFRAME)
    # get_stock_data(SYMBOL, timeframe=TIMEFRAME)
    # return
    workers = []
    if __name__ == '__main__':
        for limit in frange(103, 105, 0.5):
            w = multiprocessing.Process(
                target=worker,
                args=(limit,)
            )
            workers.append(w)

        for w in workers:
            w.start()

        for w in workers:
            w.join()
        print(1)
        # start_emas()


def test(df, pf, stop, limit, ema_short, ema_long, adx):
    df, pf = strategy.ma_crossing_adx(df, pf, ema_short, ema_long, stop, limit)
    performance = round((pf.cash / STARTING_AMOUNT * 100) - 100, 4)

    print('.', end='')
    if performance > 2:  # and pf.positive > pf.negative:
        print('')
        print(
            f'Performance: {performance} %\t- Stop:{stop}, Limit: {limit}\t- EMA short: {ema_short}, EMA long: {ema_long}, ADX: {adx},\t- {round(pf.positive / pf.negative, 2)}\t- positive: {pf.positive}, negative: {pf.negative}'
        )
    # print(f"Chart performance: \t\t {round((df['Close'].iloc[-1] - df['Close'].iloc[1]) / df['Close'].iloc[1] *100, 4)} %")
    return performance
    # print(f"Starting cash: \t\t\t {STARTING_AMOUNT}")
    # print(f"Ending cash: \t\t\t {round(pf.cash, 2)}")
    # print(f"Chart performance: \t\t {round((df['Close'].iloc[-1] - df['Close'].iloc[1]) / df['Close'].iloc[1] *100, 4)} %")
    # print(f'Algorithm performance: \t {round((pf.cash/ STARTING_AMOUNT *100) - 100, 4)} %')
    # print(f'positive: {pf.positive}, negative: {pf.negative}')


def test_single_symbol(item, stop, limit, ema_short, ema_long, chart=False):
    pf = Portfolio(STARTING_AMOUNT)

    df = dataframe.trading_data_from_csv(item, time=TIMEFRAME, add_indicators=False)
    df = df.loc[f'{sdate} 00:00:00-00:00':f'{edate} 23:00:00-00:00']

    df = indicator.exponential_moving_average(df, ema_short)
    df = indicator.exponential_moving_average(df, ema_long)
    # df = indicator.adx_indicator(df)

    df = df.rename(columns={f'close': 'Close', f'high': 'High', f'low': 'Low', f'open': 'Open'})

    performance = test(df, pf, stop, limit, ema_short, ema_long, )
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
