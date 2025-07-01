# coal-api/data.py
import pandas as pd
from importlib.resources import files


def load_dataset():
    """
    Loads the US coal plants dataset from a CSV file.

    Returns:
        pandas.DataFrame: A DataFrame containing the data from 'us_coal_plants_dataset.csv'.

    Raises:
        FileNotFoundError: If the dataset file does not exist at the specified path.
        pd.errors.EmptyDataError: If the CSV file is empty.
        pd.errors.ParserError: If the CSV file cannot be parsed.
    """
    path = files("retire.data").joinpath("resources/us_coal_plants_dataset.csv")
    return pd.read_csv(path)


def load_clean_dataset():
    """
    Loads the cleaned and scaled US coal plant dataset from a CSV file.

    Returns:
        pandas.DataFrame: A DataFrame containing the cleaned and scaled US coal plant data.

    Raises:
        FileNotFoundError: If the dataset file does not exist at the specified path.
        pd.errors.EmptyDataError: If the CSV file is empty.
        pd.errors.ParserError: If the CSV file cannot be parsed.
    """
    path = files("retire.data").joinpath(
        "resources/clean_scaled_us_coalplant_dataset.csv"
    )
    return pd.read_csv(path)


def load_projection():
    path = files("retire.data").joinpath("resources/projected_us_coalplant_dataset.csv")
    return pd.read_csv(path)
