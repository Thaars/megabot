from definitions import *


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