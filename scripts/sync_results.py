import os
import pandas as pd
from config import (
    retired_columns,
    path_to_retired_sheet,
    metrics_columns,
    path_to_metrics_sheet,
    news_columns,
    path_to_news_sheet,
)
from script_utils import get_repo_root


def sync_retiredPlants_data(columns=retired_columns):
    df = pd.read_csv(path_to_retired_sheet)[retired_columns]
    repo_root = get_repo_root()
    csv_path = os.path.join(repo_root, "retire/resources/results/retired.csv")
    df.to_csv(csv_path, index=False)


def sync_news_data(columns=news_columns):
    repo_root = get_repo_root()
    news_df = pd.read_csv(path_to_news_sheet)[columns]
    raw_df_path = os.path.join(repo_root, "retire/resources/us_coal_plants_dataset.csv")
    raw = pd.read_csv(raw_df_path)

    key = "ORISPL"

    results_extra_cols = [
        col for col in news_df.columns if col not in raw.columns and col != key
    ]

    results_subset = news_df[columns].set_index(key)

    df = raw[[key]].copy()
    df = df.set_index(key).join(results_subset, how="left")
    df = df.reset_index()
    df.index = raw.index

    csv_path = os.path.join(repo_root, "retire/resources/results/retired.csv")
    df.to_csv(csv_path, index=False)


def sync_metrics_data(columns=metrics_columns):
    repo_root = get_repo_root()
    news_df = pd.read_csv(path_to_news_sheet)[columns]
    raw_df_path = os.path.join(repo_root, "retire/resources/us_coal_plants_dataset.csv")
    raw = pd.read_csv(raw_df_path)

    key = "ORISPL"

    results_subset = news_df[columns].set_index(key)

    df = raw[[key]].copy()
    df = df.set_index(key).join(results_subset, how="left")
    df = df.reset_index()
    df.index = raw.index

    csv_path = os.path.join(repo_root, "retire/resources/results/retired.csv")
    df.to_csv(csv_path, index=False)

    def main():
        sync_retiredPlants_data()
        sync_news_data()
        sync_metrics_data()

    if __name__ == "__main__":
        main()
