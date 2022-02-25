import sys
import warnings

from definitions import *
from strategies.price_breakout import PRICE_BREAKOUT


def ma_crossing_adx(df, pf, short_term, long_term, stop, limit, indicator_type="EMA"):
    """
    simple strategy the uses two moving averages.
    The short term crossing the long term chart is an indicator for bullish/bearish
    the lower short term crosses the upper long term indicates bullish marker (vice versa for bearish)
    """

    adx_border = 17

    for (line, (index, row)) in enumerate(df.iterrows()):

        last_row = df.iloc[line - 1]

        if last_row[f'{short_term} Day {indicator_type}'] < last_row[f'{long_term} Day {indicator_type}'] and \
                row[f'{short_term} Day {indicator_type}'] > row[f'{long_term} Day {indicator_type}'] and \
                row['ADX'] > adx_border and row['DMP'] > last_row['DMP']:

            # bullish crossing
            stop_price = round(row['Close'] / 100 * stop, 2)
            limit_price = round(row['Close'] / 100 * limit, 2)

            # 2 limits
            if len(pf.orders) == 0:
                limit2_price = round(row['Close'] / 100 * (limit * 2 - 100), 2)
                pf.create_order(df, index, row['Close'], limit=limit_price, lower_stop=stop_price,
                                limit2=limit2_price, pull_up_sl=True)

            # 1 limit
            # pf.create_order(df, index, row['Close'], limit=limit_price, lower_stop=stop_price)
            continue

        # check if stop loss has passed
        pf.adjust_stop_price_for_orders(df, index)

    pf.close_all_orders(df, df['Close'].iloc[-1])

    return df, pf


def price_breakout(df, pf):
    from strategies.price_breakout import PRICE_BREAKOUT
    po = PRICE_BREAKOUT(df=df, pf=pf)
    po.prepare()
    return po.analyze()


def price_mini_wicks(df, pf):
    from strategies.price_mini_wicks import PRICE_MINI_WICKS
    po = PRICE_MINI_WICKS(df=df, pf=pf)
    po.prepare()
    return po.analyze()


def price_quick_doji(df, pf):
    from strategies.price_quick_doji import PRICE_QUICK_DOJI
    po = PRICE_QUICK_DOJI(df=df, pf=pf)
    po.prepare()
    return po.analyze()


# todo:
#   neue strategie
#   umbrella / gravestone
#   beim doji mit langem Wick zur einen und (fast) keinem Wick zur anderen Seite zeigen eine Trendwende an
#   der Kurs bewegt sich dann in Richtung des kleineren Wicks
#   Target könnte die länge des längeren Wicks sein
#   Stop Loss ebenfalls