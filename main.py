import json
import multiprocessing
import zlib

import definitions
import strategy
import dataframe
import plot
import indicator
from api import get_all_binance, get_stock_data
from db import DB
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
    db = DB().db
    # filename = get_all_binance(definitions.SYMBOL, definitions.TIMEFRAME)
    filename = get_stock_data(SYMBOL, timeframe=TIMEFRAME)
    pf, config = test(filename, definitions.PLOT)
    save_strategy(db, pf, config)
    print(f"*********************************************")
    print(f"Config: {json.dumps(config)}")
    print(f"Symbol: {SYMBOL}")
    print(f"Timeframe: {TIMEFRAME}")
    print(f"Trades: ")
    print(f"\t winning - {pf.winning}")
    print(f"\t losing - {pf.losing}")
    print(f"\t winners - {pf.winners}")
    print(f"\t losers - {pf.losers}")
    print(f"Performance: ")
    print(f'\t market: {pf.get_market_performance()}')
    print(f'\t overall: {pf.get_performance()}')
    print(f"Total: ")
    print(f'\t cash: {round(pf.cash, 2)}')
    print(f'\t ticks: {round(pf.ticks, 5)}')
    print(f'\t winning ticks: {round(pf.winning_ticks, 5)}')
    print(f'\t losing ticks: {round(pf.losing_ticks, 5)}')
    print(f'\t tick cash: {round(pf.ticks * TICK_VALUE, 5)}')
    print(f'\t max stop loss amount: {round(pf.max_stop_loss_amount, 5)}')
    print(f'\t max stop loss ticks: {round(pf.max_stop_loss_amount / TICK_SIZE, 5)}')
    print(f'\t max stop loss margin: {round((pf.max_stop_loss_amount / TICK_SIZE) * TICK_VALUE, 5)}')
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

    df = indicator.last_5_10_15_20_candles(df, filename)

    df = df.loc[f'{definitions.START_DATE} 00:00:00-00:00':f'{definitions.END_DATE} 23:00:00-00:00']

    pf = Portfolio(df, STARTING_AMOUNT)
    # df, pf, config = strategy['price_breakout'](df, pf)
    used_strategy = getattr(strategy, USED_STRATEGY)
    df, pf, config = used_strategy(df, pf)

    if chart:
        plot.plot_data(df)

    return pf, config


def save_strategy(db, pf, config):
    db_cursor = db.cursor()
    days = (END_DATE - START_DATE).days
    trading_breaks = None
    if USE_TRADING_BREAKS:
        trading_breaks = json.dumps(TRADING_BREAKS)
    general_hash_values = [
        SYMBOL,
        USED_STRATEGY,
        json.dumps(config),
        TIMEFRAME,
        TICK_SIZE,
        TICK_VALUE,
    ]
    exact_hash_values = general_hash_values + [
        f'{START_DATE}',
        f'{END_DATE}',
        COMMISSION,
        STARTING_AMOUNT,
        json.dumps(trading_breaks),
    ]
    db_cursor.executemany("insert into results("
                            "`general_hash`,"
                            "`exact_hash`,"
                            "`symbol`,"
                            "`strategy`,"
                            "`strategy_config`,"
                            "`timeframe`,"
                            "`trade_type`,"
                            "`days`,"
                            "`performance`,"
                            "`market_performance`,"
                            "`winning`,"
                            "`losing`,"
                            "`winners`,"
                            "`losers`,"
                            "`starts_at`,"
                            "`ends_at`,"
                            "`ticks`,"
                            "`winning_ticks`,"
                            "`losing_ticks`,"
                            "`tick_cash`,"
                            "`max_stop_loss_amount`,"
                            "`max_stop_loss_ticks`,"
                            "`max_stop_loss_margin`,"
                            "`tick_size`,"
                            "`tick_value`,"
                            "`trading_breaks`,"
                            "`commission`,"
                            "`start_cash`,"
                            "`end_cash`"
                          ") values("
                          "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"
                          ")", [(
                            zlib.adler32(json.dumps(general_hash_values).encode('UTF-8')) & 0xffffffff,
                            zlib.adler32(json.dumps(exact_hash_values).encode('UTF-8')) & 0xffffffff,
                            SYMBOL,
                            USED_STRATEGY,
                            json.dumps(config),
                            TIMEFRAME,
                            config['trade_type'],
                            days,
                            pf.get_performance(),
                            pf.get_market_performance(),
                            json.dumps(pf.winning),
                            json.dumps(pf.losing),
                            json.dumps(pf.winners),
                            json.dumps(pf.losers),
                            f'{START_DATE}',
                            f'{END_DATE}',
                            float(round(pf.ticks, 5)),
                            float(round(pf.winning_ticks, 5)),
                            float(round(pf.losing_ticks, 5)),
                            float(round(pf.ticks * TICK_VALUE, 5)),
                            float(round(pf.max_stop_loss_amount, 5)),
                            float(round(pf.max_stop_loss_amount / TICK_SIZE, 5)),
                            float(round((pf.max_stop_loss_amount / TICK_SIZE) * TICK_VALUE, 5)),
                            float(TICK_SIZE),
                            float(TICK_VALUE),
                            json.dumps(trading_breaks),
                            float(COMMISSION),
                            float(STARTING_AMOUNT),
                            float(round(pf.cash, 2))
                          )])
    db.commit()


main()
