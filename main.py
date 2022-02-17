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


sdate = date(2022, 2, 1)  # start date
edate = date(2022, 2, 7)  # edate = date(2018, 8, 15)
TIMEFRAME = "5m"
SYMBOL = 'BTCUSDT'


def frange(start, stop, step=1.0):
    while start <= stop:
        yield start
        start += step


def worker():
    print(f'Worker spawned')
    test(definitions.PLOT)
    print(f"Worker finished the work")


def main():
    get_all_binance(definitions.SYMBOL, definitions.TIMEFRAME)
    # get_stock_data(SYMBOL, timeframe=TIMEFRAME)
    pf = test(definitions.PLOT)
    print(f"*********************************************")
    print(f"Trades: ")
    print(f"\t winning - {pf.winning}")
    print(f"\t losing - {pf.losing}")
    print(f'Market performance: {pf.get_market_performance()}')
    print(f'Overall performance: {pf.get_performance()}')
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


def test(chart=False):
    filename = 'data_with_indicators/%s-%s-%s-%s-data.csv' % (
        definitions.SYMBOL, definitions.TIMEFRAME, definitions.BINANCE_DATA_FROM, definitions.BINANCE_DATA_TO
    )

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
