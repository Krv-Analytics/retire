# retire/data.py

import pandas as pd
import networkx as nx
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

    """
    path = files("retire.data").joinpath(
        "resources/clean_scaled_us_coalplant_dataset.csv"
    )
    return pd.read_csv(path)


def load_projection():
    """
    Loads the projected US coal plant dataset from a CSV file.

    Returns:
        pandas.DataFrame: A DataFrame containing the projected US coal plant data.

    """
    path = files("retire.data").joinpath("resources/projected_us_coalplant_dataset.csv")
    return pd.read_csv(path)


def load_graph():
    """
    Loads a graph from CSV files containing node and edge data.

    This function reads node and edge information from CSV files located in the
    'resources/graph' directory within the 'retire.data' package. It constructs a
    NetworkX graph, adding nodes and edges along with their associated attributes.

    Returns:
        networkx.Graph: A graph object with nodes and edges populated from the CSV files.

    """

    node_path = files("retire.data").joinpath("resources/graph/graphnode_df.csv")
    edge_path = files("retire.data").joinpath("resources/graph/graphedge_df.csv")

    # Load dataframes
    node_df = pd.read_csv(node_path)
    edge_df = pd.read_csv(edge_path)

    # Initialize graph
    G = nx.Graph()

    # Add nodes with attributes
    for _, row in node_df.iterrows():
        node_id = row["node"] if "node" in row else row[0]
        attrs = row.drop("node").to_dict() if "node" in row else row[1:].to_dict()
        G.add_node(node_id, **attrs)

    # Add edges with attributes
    G.add_edges_from(
        [
            (row["source"], row["target"], row.drop(["source", "target"]).to_dict())
            for _, row in edge_df.iterrows()
        ]
    )

    return G
