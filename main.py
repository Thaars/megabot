import json
import multiprocessing
import warnings
import zlib

import definitions
import strategy
import dataframe
import plot
import indicator
from api import get_all_binance, get_stock_data, get_tradovate_data
from db import DB
from portfolio import Portfolio
from definitions import *
from datetime import date


def frange(start, stop, step=1.0):
    while start <= stop:
        yield start
        start += step


def worker():
    print(f'Worker spawned')
    run_back_test(definitions.PLOT)
    print(f"Worker finished the work")


def main():
    db = DB().db
    # filename = get_tradovate_data(definitions.SYMBOL, definitions.TIMEFRAME)
    filename = get_all_binance(definitions.SYMBOL, definitions.TIMEFRAME)
    # # filename = get_stock_data(SYMBOL, timeframe=TIMEFRAME)
    pf, config = run_back_test(filename, definitions.PLOT)
    save_strategy(db, pf, config)
    print(f"*********************************************")
    print(f"Config: {json.dumps(config)}")
    print(f"Symbol: {SYMBOL}")
    print(f"Timeframe: {TIMEFRAME}")
    print(f"Trades: ")
    for cycle in pf.cycles_for_stats:
        print(json.dumps(cycle['stats']))
    print(f"On hold: ")
    sum_bound_cash = 0
    sum_on_hold = 0
    # calc trades which are on hold because the buying price was never reached again in this timeframe
    for cycle in pf.cycles_for_stats:
        if len(cycle['orders']) > 0:
            first_bought_at = 0
            last_bought_at = 0
            sum_orders = 0
            sum_units = 0
            for order in cycle['orders']:
                if first_bought_at == 0:
                    first_bought_at = str(order['index'].day) + '.' + str(order['index'].month) + '.' \
                                      + str(order['index'].year) + '. ' + str(order['index'].hour) + 'h'
                # last buy will be overwritten each time, so it's the last at the end
                last_bought_at = str(order['index'].day) + '.' + str(order['index'].month) + '.' \
                                      + str(order['index'].year) + '. ' + str(order['index'].hour) + 'h'
                sum_units += order['units']
                sum_orders += order['units'] * order['buying_price']
            crypto_on_hold = {
                'units': sum_units,
                'average_buying_price': round(sum_orders / sum_units, 2),
                'average_buying_costs': round(sum_orders / len(cycle['orders']), 2),
                'bound_cash': round(sum_orders, 2),
                'first_bought_at': first_bought_at,
                'last_bought_at': last_bought_at
            }
            sum_bound_cash += sum_orders
            sum_on_hold += 1
            print(f'\t crypto on hold: {json.dumps(crypto_on_hold)}')
    print(f"General: ")
    print(f'\t holds: {sum_on_hold}')
    print(f'\t cycles: {len(pf.cycles_for_stats)}')
    print(f'\t orders: {pf.order_count}')
    print(f"Total: ")
    print(f'\t cash: {round(pf.cash, 2)}')
    print(f'\t bound cash: {round(sum_bound_cash, 2)} (average buying price)')
    print(f'\t total cash: {round(pf.cash + sum_bound_cash, 2)}')
    print(f"Performance: ")
    print(f'\t market: {pf.get_market_performance()}')
    print(f'\t overall: {pf.get_performance(round(pf.cash + sum_bound_cash, 2))}')
    return


def run_back_test(filename, chart=False):
    df = dataframe.trading_data_from_csv(filename)

    df = indicator.last_5_10_15_20_candles(df, filename)
    df = indicator.aroon(df, filename, definitions.AROON_PERIOD)
    df = indicator.ma_cross(df, filename, definitions.MA_FAST_PERIOD, definitions.MA_SLOW_PERIOD)
    df = indicator.fractals(df, filename, definitions.FRACTALS_PERIOD)

    df = df.loc[f'{definitions.START_DATE}':f'{definitions.END_DATE}']

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
        COMMISSION_FACTOR,
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
                            "`largest_loser_series`,"
                            "`starts_at`,"
                            "`ends_at`,"
                            "`ticks`,"
                            "`winning_ticks`,"
                            "`losing_ticks`,"
                            "`tick_cash`,"
                            "`lowest_tick_cash`,"
                            "`max_stop_loss_amount`,"
                            "`max_stop_loss_ticks`,"
                            "`max_stop_loss_margin`,"
                            "`tick_size`,"
                            "`tick_value`,"
                            "`trading_breaks`,"
                            "`commission_factor`,"
                            "`commission_value`,"
                            "`start_cash`,"
                            "`end_cash`"
                          ") values("
                          "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"
                          ")", [(
                            zlib.adler32(json.dumps(general_hash_values).encode('UTF-8')) & 0xffffffff,
                            zlib.adler32(json.dumps(exact_hash_values).encode('UTF-8')) & 0xffffffff,
                            SYMBOL,
                            USED_STRATEGY,
                            json.dumps(config),
                            TIMEFRAME,
                            '',
                            days,
                            pf.get_performance(),
                            pf.get_market_performance(),
                            '',
                            '',
                            '',
                            '',
                            '',
                            f'{START_DATE}',
                            f'{END_DATE}',
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            '',
                            float(COMMISSION_FACTOR),
                            0,
                            float(STARTING_AMOUNT),
                            float(round(pf.cash, 2))
                          )])
    db.commit()


main()
