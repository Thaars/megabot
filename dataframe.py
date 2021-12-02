import pandas as pd

def trading_data_from_csv(symbol, time="5m", add_indicators=False):
    df = pd.read_csv(f"data_with_indicators/{symbol}-{time}-data.csv", delimiter=";")
    df = df.set_index(['Datetime'])
    df.index = pd.to_datetime(df.index, utc=True)
    return df
