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

# todo: neue strategie:
#   Candle Wicks dürfen beide max. 5 oder 10 Prozent vom Body lang sein
#   Body darf nicht mehr als doppelt so groß sein wie der gößte Body der letzten 5 Candles
#   Stop Loss: 1x Candle Body
#   Target: 1x Candle Body
#   Short + Long
#   5m, 10m, 15m testen ggf. auch mal 1m oder 3m
#     Gold: ggf. 1m oder 2m, weil bei 5m immer längere Wicks zu sehen waren
#     BTC: scheint mit 5m ganz gut zu sein
#   DF zusätzlich anreichern mit den letzten 5 Kerzen

