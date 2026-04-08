# data_loader.py

import pandas as pd


def load_data(data_url: str) -> pd.DataFrame:
    return pd.read_csv(data_url)

