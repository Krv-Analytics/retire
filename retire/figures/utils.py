import pandas as pd
import networkx as nx


def prepare_bar_annotations(df, label_map, buffer=2):
    """Create Plotly-compatible annotations for each bar category."""
    return [
        dict(
            x=label,
            y=df[df["Target"] == label]["Value"].sum() + buffer,
            text=html_label,
            showarrow=False,
        )
        for label, html_label in label_map.items()
    ]


def get_key_nodes(percent_retiring_dict, threshold=0.5):
    """
    Return nodes with retirement percent above a threshold.
    """
    return {node: val for node, val in percent_retiring_dict.items() if val > threshold}


def compute_retirement_by_node(G, df, col="Percent Capacity Retiring"):
    """
    For each node in the graph, calculate the average retirement percent
    from the associated plants (via membership indices).
    """
    percent_retiring = {}
    for node in G.nodes():
        indices = G.nodes[node].get("membership", [])
        if indices:
            percent_retiring[node] = df.loc[indices, col].mean()
        else:
            percent_retiring[node] = 0.0
    return percent_retiring


def process_group_sankey_df(
    G: nx.Graph,
    df: pd.DataFrame,
    group_num: int,
    threshold: float = 0.5,
    return_all: bool = False,
) -> pd.DataFrame:
    """Builds Sankey-ready data for one group."""

    # Extract the subgraph for the group
    subgraph = list(nx.connected_components(G))[group_num]
    subG = G.subgraph(subgraph).copy()

    # Identify targets
    retiring_pct = compute_retirement_by_node(subG, df)
    targets = list(get_key_nodes(retiring_pct, threshold).keys())

    # Compute shortest distances to targets
    dist_data = {
        node: min(
            (
                nx.shortest_path_length(subG, source=node, target=t, weight="weight")
                for t in targets
            ),
            default=float("inf"),
        )
        for node in subG.nodes
    }

    # Collect node data
    dfs = []
    for node, dist in dist_data.items():
        node_df = df.loc[subG.nodes[node]["membership"]].copy()
        node_df["Distance Score"] = dist
        dfs.append(node_df)

    out_df = (
        pd.concat(dfs)
        .sort_values("Distance Score")
        .drop_duplicates("ORISPL")
        .reset_index(drop=True)
    )

    # Bin and label
    bins = [-float("inf"), 0, 1 / 3, 2 / 3, float("inf")]
    labels = ["High Proximity", "Mid-Proximity", "Low-Proximity", "Far from Retirement"]
    out_df["Target"] = pd.cut(out_df["Distance Score"], bins=bins, labels=labels)
    out_df["Target"] = out_df["Target"].astype(str)
    out_df.loc[out_df["ret_STATUS"] == 2, "Target"] = "Retiring"

    # Final formatting
    order = ["Retiring"] + labels
    out_df["Target"] = pd.Categorical(out_df["Target"], categories=order, ordered=True)
    out_df["Source"] = group_num

    if return_all:
        return out_df

    # Sankey format
    return (
        out_df.groupby("Target", observed=False)["ORISPL"]
        .count()
        .reset_index()
        .rename(columns={"ORISPL": "Value"})
        .assign(Source=group_num)
    )


def build_group_sankey(
    G: nx.Graph,
    df: pd.DataFrame,
    group_range: range = range(8),
    return_all: bool = False,
) -> pd.DataFrame:
    """Runs process_group_sankey_df across multiple groups and combines output."""
    return pd.concat(
        [
            process_group_sankey_df(G, df, group_num, return_all=return_all).assign(
                group=group_num
            )
            for group_num in group_range
        ],
        ignore_index=True,
    )


def reduce_opacity(color: str, opacity: float) -> str:
    rgb = color.split("(")[1].split(")")[0]
    return f"rgba({rgb}, {opacity})"


def create_color_mapping(
    sources, targets, color_scale, target_color_mapping, opacity=0.7
):
    all_nodes = sources.union(targets)
    faded_colors = [reduce_opacity(c, opacity) for c in color_scale]

    mapping = {
        node: faded_colors[i % len(faded_colors)] for i, node in enumerate(all_nodes)
    }
    mapping.update(target_color_mapping)  # Overwrite targets with specified colors
    return mapping


def build_index_mappings(sources, targets):
    sources_dict = {node: i for i, node in enumerate(sources)}
    targets_dict = {node: i + len(sources) for i, node in enumerate(targets)}
    return sources_dict, targets_dict
