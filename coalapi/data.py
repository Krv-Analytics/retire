# coal-api/data.py
from importlib.resources import files
import pandas as pd


def load_dataset():
    path = files("coal-api.data").joinpath("us_coal_plants_dataset.csv")
    return pd.read_csv(path)
