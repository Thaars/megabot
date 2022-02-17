import multiprocessing

import definitions
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


def frange(start, stop, step=1.0):
    while start <= stop:
        yield start
        start += step


def worker():
    print(f'Worker spawned')
    test(definitions.PLOT)
    print(f"Worker finished the work")


def main():
    # filename = get_all_binance(definitions.SYMBOL, definitions.TIMEFRAME)
    filename = get_stock_data(SYMBOL, timeframe=TIMEFRAME)
    pf = test(filename, definitions.PLOT)
    print(f"*********************************************")
    print(f"Trades: ")
    print(f"\t winning - {pf.winning}")
    print(f"\t losing - {pf.losing}")
    print(f"Performance: ")
    print(f'\t market: {pf.get_market_performance()}')
    print(f'\t overall: {pf.get_performance()}')
    print(f"Cash: ")
    print(f'\t cash: {pf.cash}')
    print(f'\t points: {pf.points}')
    return
    # workers = []
    # if __name__ == '__main__':
    #     # for limit in frange(103, 105, 0.5):
    #     w = multiprocessing.Process(
    #         target=worker,
    #         args=()
    #     )
    #     workers.append(w)
    #
    #     for w in workers:
    #         w.start()
    #
    #     for w in workers:
    #         w.join()
    #     print(1)


def test(filename, chart=False):
    df = dataframe.trading_data_from_csv(filename)

    df = indicator.last_10_15_20_candles(df, filename)

    df = df.loc[f'{definitions.START_DATE} 00:00:00-00:00':f'{definitions.END_DATE} 23:00:00-00:00']

    pf = Portfolio(df, STARTING_AMOUNT)
    df, pf = strategy.price_outbreak(df, pf)
    performance = round((pf.cash / STARTING_AMOUNT * 100) - 100, 4)

    if chart:
        plot.plot_data(df)

    return pf


main()
