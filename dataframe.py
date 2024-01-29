import pandas as pd

def trading_data_from_csv(filename):
    df = pd.read_csv(filename, delimiter=";")
    df = df.set_index(['datetime'])
    df.index = pd.to_datetime(df.index, utc=True)
    return df
