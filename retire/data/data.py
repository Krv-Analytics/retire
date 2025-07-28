# retire/data.py

import ast
import pandas as pd
import networkx as nx
from importlib.resources import files


def load_dataset():
    """
    Load the US coal plants dataset from the package resources.

    Returns
    -------
    pandas.DataFrame
        Complete US coal plants dataset containing plant characteristics,
        retirement status, contextual vulnerabilities, and associated metadata.
        Includes columns for plant location, capacity, age, retirement planning,
        economic factors, and environmental considerations.

    Raises
    ------
    FileNotFoundError
        If the dataset file does not exist at the specified path.
    pd.errors.EmptyDataError
        If the CSV file is empty.
    pd.errors.ParserError
        If the CSV file cannot be parsed.

    Examples
    --------
    >>> from retire.data import load_dataset
    >>> df = load_dataset()
    >>> print(df.shape)
    (914, 45)
    >>> print(df.columns[:5].tolist())
    ['Plant Name', 'ORISPL', 'State', 'County', 'LAT']
    """
    path = files("retire").joinpath("resources/us_coal_plants_dataset.csv")
    return pd.read_csv(path)


def load_clean_dataset():
    """
    Load the cleaned and scaled US coal plant dataset.

    This dataset has undergone preprocessing including missing value imputation,
    feature scaling, and normalization for use in machine learning models and
    statistical analysis.

    Returns
    -------
    pandas.DataFrame
        Cleaned and scaled coal plant dataset with standardized numerical
        features and processed categorical variables. All features are
        normalized to facilitate clustering and similarity analysis.

    Examples
    --------
    >>> from retire.data import load_clean_dataset
    >>> clean_df = load_clean_dataset()
    >>> print(clean_df.dtypes.value_counts())
    float64    42
    int64       3
    dtype: int64
    """
    path = files("retire").joinpath("resources/clean_scaled_us_coalplant_dataset.csv")
    return pd.read_csv(path)


def load_projection():
    """
    Load the projected US coal plant dataset with future scenario modeling.

    This dataset contains projections and forecasts for coal plant operations
    under various policy and economic scenarios, including retirement timing
    predictions and capacity factor estimates.

    Returns
    -------
    pandas.DataFrame
        Projected coal plant dataset with scenario-based forecasts for
        retirement timing, capacity utilization, and economic viability
        under different policy environments.

    Examples
    --------
    >>> from retire.data import load_projection
    >>> proj_df = load_projection()
    >>> scenario_cols = [col for col in proj_df.columns if 'scenario' in col.lower()]
    >>> print(f"Available scenarios: {len(scenario_cols)}")
    """
    path = files("retire").joinpath("resources/projected_us_coalplant_dataset.csv")
    return pd.read_csv(path)


def load_graph():
    """
    Load the coal plant network graph from package resources.

    Constructs a NetworkX graph representing relationships between coal plant
    clusters based on similarity metrics and contextual factors. Nodes represent
    plant clusters, and edges represent similarity relationships weighted by
    various plant characteristics.

    Returns
    -------
    networkx.Graph
        Network graph with nodes representing coal plant clusters and edges
        representing similarity relationships. Node attributes include:
        - membership: list of plant indices belonging to the cluster
        - cluster_id: unique identifier for the cluster
        Edge attributes include:
        - weight: similarity strength between clusters

    Raises
    ------
    FileNotFoundError
        If the graph node or edge CSV files do not exist.
    ValueError
        If the membership field cannot be parsed as a list.

    Examples
    --------
    >>> from retire.data import load_graph
    >>> G = load_graph()
    >>> print(f"Graph has {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")
    Graph has 314 nodes and 1247 edges
    >>> # Check node attributes
    >>> node_attrs = list(G.nodes(data=True))[0]
    >>> print(f"Node attributes: {list(node_attrs[1].keys())}")
    """

    node_path = files("retire").joinpath("resources/graph/graphnode_df.csv")
    edge_path = files("retire").joinpath("resources/graph/graphedge_df.csv")

    # Load dataframes
    node_df = pd.read_csv(node_path)
    edge_df = pd.read_csv(edge_path)

    # Initialize graph
    G = nx.Graph()

    # Add nodes with attributes (including parsing membership if needed)
    for _, row in node_df.iterrows():
        node_id = row["node"] if "node" in row else row[0]
        attrs = row.drop("node").to_dict() if "node" in row else row[1:].to_dict()

        # Safely parse membership field if it's a string
        if "membership" in attrs and isinstance(attrs["membership"], str):
            try:
                attrs["membership"] = ast.literal_eval(attrs["membership"])
            except (ValueError, SyntaxError):
                attrs["membership"] = []  # or raise an error if preferred

        G.add_node(node_id, **attrs)

    # Add edges with attributes
    G.add_edges_from(
        [
            (row["source"], row["target"], row.drop(["source", "target"]).to_dict())
            for _, row in edge_df.iterrows()
        ]
    )

    return G


def load_generator_level_dataset():
    """
    Load the generator-level US coal plants dataset.

    Provides detailed information at the individual generator unit level,
    including technical specifications, operational history, and retirement
    planning for each coal-fired generating unit in the US fleet.

    Returns
    -------
    pandas.DataFrame
        Generator-level dataset with detailed technical and operational
        information for individual coal-fired generating units. Includes
        capacity, age, efficiency metrics, emissions data, and retirement
        status for each generator.

    Raises
    ------
    FileNotFoundError
        If the dataset file does not exist at the specified path.
    pd.errors.EmptyDataError
        If the CSV file is empty.
    pd.errors.ParserError
        If the CSV file cannot be parsed.

    Examples
    --------
    >>> from retire.data import load_generator_level_dataset
    >>> gen_df = load_generator_level_dataset()
    >>> print(f"Total generators: {len(gen_df)}")
    >>> # Group by plant to see generator counts per plant
    >>> gens_per_plant = gen_df.groupby('ORISPL').size()
    >>> print(f"Average generators per plant: {gens_per_plant.mean():.1f}")
    """
    path = files("retire").joinpath("resources/generator_level_dataset.csv")
    return pd.read_csv(path)
