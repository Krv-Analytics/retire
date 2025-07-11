# figures/coal_figure.py

import numpy as np
import pandas as pd
import seaborn as sns
import networkx as nx
from typing import Dict
from matplotlib import rcParams
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.lines import Line2D
import matplotlib.patches as patches
from matplotlib.colors import Normalize
from sklearn.preprocessing import StandardScaler


class PlotKit:

    def __init__(self, G: nx.Graph, raw_df: pd.DataFrame):
        self.G = G
        self.raw_df = raw_df

    def drawGraph(
        self,
        col: str = None,
        pos: Dict[str, np.ndarray] = None,
        title: str = None,
        size: tuple = (8, 6),
        show_colorbar: bool = False,
        color_method: str = "average",
        show_node_labels: bool = False,
    ):
        """
        Visualize a THEMA-generated NetworkX graph with optional node coloring.

        Parameters
        ----------
        col : str, optional
            Column in raw data to use for node coloring when `color_method='average'`.
            If None, no coloring is applied.
        pos : dict, optional
            Node positions for layout. If None, spring layout is used.
        title: str, optional
            Title for the plot. If None, no title is displayed.
        size : tuple, default=(8, 6)
            Figure size in inches.
        show_colorbar : bool, default=False
            Whether to display a colorbar (only used if col is provided).
        color_method : {"average", "community"}, default="average"
            Method for coloring nodes: by attribute average or by community.
        show_node_labels : bool, default=False
            Whether to display node labels.

        Returns
        -------
        fig : matplotlib.figure.Figure
            The created matplotlib figure.
        ax : matplotlib.axes.Axes
            The created matplotlib axes.
        """

        return self.drawGraph_helper(
            G=self.G,
            col=col,
            pos=pos,
            size=size,
            show_colorbar=show_colorbar,
            color_method=color_method,
            show_node_labels=show_node_labels,
            title=title,
        )

    def drawComponent(
        self,
        component: int,
        col: str = "ret_STATUS",
        pos: Dict[str, np.ndarray] = None,
        title=None,
        size: tuple = (8, 6),
        show_colorbar: bool = False,
        color_method: str = "average",
        show_node_labels: bool = False,
    ):
        """
        Draws a specific connected component of the graph.

        Parameters
        ----------
        col : str, optional
            Column in raw data to use for node coloring when `color_method='average'`.
            If None, no coloring is applied.
        pos : dict, optional
            Node positions for layout. If None, spring layout is used.
        title: str, optional
            Title for the plot. If None, no title is displayed.
        size : tuple, default=(8, 6)
            Figure size in inches.
        show_colorbar : bool, default=False
            Whether to display a colorbar (only used if col is provided).
        color_method : {"average", "community"}, default="average"
            Method for coloring nodes: by attribute average or by community.
        show_node_labels : bool, default=False
            Whether to display node labels.

        Returns
        -------
        fig : matplotlib.figure.Figure
            The created matplotlib figure.
        ax : matplotlib.axes.Axes
            The created matplotlib axes.
        """
        comp_obj = nx.connected_components(self.G)
        components = [self.G.subgraph(c).copy() for c in comp_obj]
        subGraph = components[component]
        return self.drawGraph_helper(
            G=subGraph,
            col=col,
            pos=pos,
            title=title,
            size=size,
            show_colorbar=show_colorbar,
            color_method=color_method,
            show_node_labels=show_node_labels,
        )

    def drawPathDistance(
        self,
        component: int,
        targets: Dict[str, float],
        distances_dict: Dict[str, float],
        title="",
        seed=5,
        show_colorbar=True,
        size_by_degree=True,
        scaled_legend=False,
        vmax=2.5,
        figsize=(10, 4),
    ):
        """
        Visualizes the shortest path distances from all nodes to a set of target nodes within a specified connected component of the graph.

        Parameters:
            component (int): Index of the connected component to visualize.
            targets (Dict[str, float]): Dictionary of target node identifiers (keys) and their associated values.
            distances_dict (Dict[str, float]): Dictionary mapping node identifiers to their shortest path distance to the nearest target node.
            title (str, optional): Title for the plot. Defaults to "".
            seed (int, optional): Seed for the spring layout randomization. Defaults to 5.
            show_colorbar (bool, optional): Whether to display a colorbar indicating distance values. Defaults to True.
            size_by_degree (bool, optional): If True, node sizes are scaled by their degree; otherwise, a fixed size is used. Defaults to True.
            scaled_legend (bool, optional): If True, color normalization uses a fixed range [0, vmax]; otherwise, uses the min and max of distances_dict. Defaults to False.
            vmax (float, optional): Maximum value for color normalization when scaled_legend is True. Defaults to 2.5.
            figsize (tuple, optional): Size of the figure in inches (width, height). Defaults to (10, 4).

        Returns:
            tuple: (fig, ax) where fig is the matplotlib Figure object and ax is the Axes object.
        """
        comp_obj = nx.connected_components(self.G)
        components = [self.G.subgraph(c).copy() for c in comp_obj]
        subGraph = components[component]
        fig, ax = plt.subplots(figsize=figsize, dpi=500)
        pos = nx.spring_layout(subGraph, k=0.15, seed=seed)

        # Normalize color range
        if scaled_legend:
            norm = Normalize(vmin=0, vmax=vmax)
        else:
            norm = Normalize(
                vmin=min(distances_dict.values()), vmax=max(distances_dict.values())
            )

        node_colors = [
            plt.cm.tab20c(norm(distances_dict[node])) for node in subGraph.nodes()
        ]

        # Node size
        if size_by_degree:
            node_sizes = [len(subGraph[node]) * 15 for node in subGraph.nodes()]
        else:
            node_sizes = 50

        nx.draw_networkx_edges(subGraph, pos, ax=ax, width=0.5, alpha=0.5)
        nx.draw_networkx_nodes(
            subGraph,
            pos,
            node_color=node_colors,
            node_size=node_sizes,
            edgecolors="white",
            ax=ax,
        )

        # Highlight target nodes
        nx.draw_networkx_nodes(
            subGraph,
            pos,
            nodelist=targets,
            node_color="#3182BD",
            edgecolors="black",
            node_size=150,
            ax=ax,
        )
        for node in targets:
            ax.text(
                pos[node][0],
                pos[node][1],
                "T",
                color="white",
                fontsize=6,
                ha="center",
                va="center",
                fontweight="bold",
            )

        if show_colorbar:
            sm = plt.cm.ScalarMappable(cmap=plt.cm.tab20c, norm=norm)
            sm.set_array([])
            plt.colorbar(sm, ax=ax, label="Distance to Nearest Target", shrink=0.8)

        ax.set_title(title)
        ax.axis("off")

        return fig, ax

    def drawHeatMap(self, config: Dict):
        """
        Generates and displays a heatmap visualization of grouped and normalized data with annotated values and category boxes.

        Parameters
        ----------
        config : dict
            Configuration dictionary containing:
                - "aggregations": dict
                    Aggregation functions to apply when grouping the data.
                - "derived_columns": list of dict
                    Each dict should have:
                        - "name": str, name of the derived column.
                        - "formula": callable, function to compute the derived column.
                        - "input": str, either "raw" or "group" to specify the source DataFrame.
                - "renaming": dict
                    Mapping of column names for renaming after aggregation.
                - "categories": dict
                    Mapping of category labels to lists of column names to group and box in the heatmap.

        Returns
        -------
        fig : matplotlib.figure.Figure
            The matplotlib Figure object containing the heatmap.
        ax : matplotlib.axes.Axes
            The matplotlib Axes object containing the heatmap.

        Notes
        -----
        - The function normalizes the selected columns using StandardScaler before plotting.
        - Annotates each heatmap cell with the original (unnormalized) value, formatted for readability.
        - Draws boxes around columns belonging to the same category and labels them.
        - Customizes plot appearance using rcParams and seaborn styling.
        """

        df = self.assign_group_ids_to_rawdf()
        group_df = df.groupby("Group").agg(config["aggregations"])

        # --- Derived columns ---
        for col in config["derived_columns"]:
            source_df = df if col.get("input", "group") == "raw" else group_df
            group_df[col["name"]] = col["formula"](source_df)

        # --- Rename ---
        group_df = group_df.rename(columns=config["renaming"])

        # --- Column selection ---
        all_columns = [col for group in config["categories"].values() for col in group]
        df_plot = group_df[all_columns].copy()

        # --- Normalize ---
        df_norm = pd.DataFrame(
            StandardScaler().fit_transform(df_plot),
            index=df_plot.index,
            columns=df_plot.columns,
        )

        # --- Plotting setup ---
        rcParams.update(
            {
                "font.family": "Arial",
                "axes.labelsize": 12,
                "axes.titlesize": 14,
                "xtick.labelsize": 10,
                "ytick.labelsize": 10,
                "legend.fontsize": 10,
            }
        )

        fig, ax = plt.subplots(figsize=(12, 3), dpi=300)
        sns.heatmap(
            df_norm,
            annot=df_plot,
            fmt=".2f",
            cbar=False,
            annot_kws={"size": 8},
            cmap="coolwarm",
            linewidths=0.5,
            ax=ax,
        )

        # Format annotations nicely
        for text in ax.texts:
            try:
                val = float(text.get_text().replace(",", ""))
                text.set_text(f"{val:,.2f}" if abs(val) < 10000 else f"{val:,.0f}")
                text.set_fontsize(6 if abs(val) > 9999 else 7)
            except ValueError:
                pass

        # --- Category boxes ---
        col_to_idx = {col: i for i, col in enumerate(df_plot.columns)}
        for label, cols in config["categories"].items():
            start = col_to_idx[cols[0]]
            end = col_to_idx[cols[-1]]
            ax.add_patch(
                patches.Rectangle(
                    (start, 0),
                    end - start + 1,
                    len(df_plot),
                    fill=False,
                    edgecolor="black",
                    linewidth=1,
                )
            )
            ax.text(
                (start + end + 1) / 2,
                -0.4,
                label,
                ha="center",
                fontsize=9,
                bbox=dict(facecolor="white", edgecolor="none", pad=0),
            )

        ax.set_xticklabels(ax.get_xticklabels(), rotation=35, ha="right", fontsize=8)
        ax.set_yticklabels(ax.get_yticklabels(), rotation=0, ha="right", fontsize=10)
        ax.set_ylabel("Group", fontsize=10)
        plt.show()

        return fig, ax

    def drawDotPlot(self, clean_df, config, connected_lines=False):
        """
        Draws a dot plot visualizing feature values across groups, with dot color representing normalized values and dot size representing standard deviation.

        Parameters
        ----------
        clean_df : pandas.DataFrame
            The cleaned DataFrame containing the data to plot. Must include columns for group assignment and the specified features.
        config : dict
            Configuration dictionary with the following keys:
                - "features": list of str, feature column names to plot.
                - "feature_labels": dict, optional, mapping of feature names to display labels.
                - "color_map": str, optional, name of the matplotlib colormap to use (default: "coolwarm").
                - "dot_size_range": tuple, optional, (min_size, max_size) for dot sizes (default: (10, 650)).
                - "normalize_feature": callable, optional, function to normalize feature values (default: identity).
        connected_lines : bool, optional
            If True, draws faint lines connecting dots of the same feature across groups (default: False).

        Returns
        -------
        fig : matplotlib.figure.Figure
            The matplotlib Figure object containing the plot.
        ax : matplotlib.axes.Axes
            The matplotlib Axes object of the plot.

        Notes
        -----
        - Each dot represents a feature value for a group.
        - Dot color encodes the normalized feature value.
        - Dot size encodes the standard deviation of the feature within the group.
        - A legend for dot sizes (standard deviation) and a colorbar for normalized values are included.
        """
        features = config["features"]
        label_map = config.get("feature_labels", {})
        cmap = plt.get_cmap(config.get("color_map", "coolwarm"))
        size_min, size_max = config.get("dot_size_range", (10, 650))

        df = self.assign_group_ids_to_cleandf(clean_df)
        df = df[~df["Group"].isna()]
        grouped_std = df.groupby("Group")[features].std()
        normalize_fn = config.get("normalize_feature", lambda s: s)

        df_long = df.melt(
            id_vars="Group",
            value_vars=features,
            var_name="Feature",
            value_name="Value",
        )
        df_long["Normalized Value"] = df_long.groupby("Feature")["Value"].transform(
            normalize_fn
        )
        std_melt = grouped_std.reset_index().melt(
            id_vars="Group", var_name="Feature", value_name="StdDev"
        )
        df_long = df_long.merge(std_melt, on=["Group", "Feature"], how="left")

        df_long["Feature"] = df_long["Feature"].replace(label_map)

        # --- Plotting ---
        rcParams.update(
            {
                "font.family": "Arial",
                "axes.labelsize": 12,
                "axes.titlesize": 14,
                "xtick.labelsize": 10,
                "ytick.labelsize": 10,
                "legend.fontsize": 10,
                "grid.color": "gray",
                "grid.linestyle": "--",
                "grid.linewidth": 0.5,
            }
        )

        fig, ax = plt.subplots(figsize=(12, 5), dpi=300)

        if connected_lines:
            for feature in df_long["Feature"].unique():
                feature_data = df_long[df_long["Feature"] == feature]
                ax.plot(
                    feature_data["Group"],
                    feature_data["Value"],
                    color="lightgray",
                    linewidth=0.5,
                    alpha=0.6,
                )

        norm = mcolors.Normalize(vmin=0, vmax=1)
        scatter = sns.scatterplot(
            data=df_long,
            x="Group",
            y="Feature",
            hue="Normalized Value",
            size="StdDev",
            sizes=(size_min, size_max),
            palette=cmap,
            edgecolor="none",
            alpha=0.7,
            legend=False,
            ax=ax,
        )

        sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
        sm.set_array([])
        cbar = plt.colorbar(sm, ax=ax, pad=0.02, fraction=0.05, shrink=0.8)
        cbar.set_label("Normalized Value", fontsize=10)
        cbar.set_ticks([])

        ax.set_xlabel("Group", labelpad=4)
        ax.set_ylabel("")
        ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.3)
        ax.set_xticks(sorted(df["Group"].unique()))

        handles = [
            Line2D(
                [0],
                [0],
                marker="o",
                color="w",
                markerfacecolor="gray",
                markersize=np.sqrt(100),
                label="Low Std. Dev",
            ),
            Line2D(
                [0],
                [0],
                marker="o",
                color="w",
                markerfacecolor="gray",
                markersize=np.sqrt(300),
                label="Med Std. Dev",
            ),
            Line2D(
                [0],
                [0],
                marker="o",
                color="w",
                markerfacecolor="gray",
                markersize=np.sqrt(650),
                label="High Std. Dev",
            ),
        ]
        ax.legend(
            handles=handles,
            ncol=3,
            bbox_to_anchor=(0.16, -0.2),
            loc="center",
            frameon=False,
        )

        plt.tight_layout()
        plt.show()
        return fig, ax

    # ╭────────────────────────────────╮
    # │   Helper Functions             |
    # ╰────────────────────────────────╯

    def drawGraph_helper(
        self,
        G: nx.Graph,
        col: str = None,
        pos: Dict[str, np.ndarray] = None,
        title: str = None,
        size: tuple = (8, 6),
        show_colorbar: bool = False,
        color_method: str = "average",
        show_node_labels: bool = False,
    ):
        """
        Helper function for visualizing a NetworkX graph with optional node coloring and labeling.

        This function is used internally by both `drawGraph` and `drawComponent` to handle the core plotting logic,
        including node coloring, sizing, layout, and optional colorbar and labels.

        Parameters
        ----------
        G : nx.Graph
            The NetworkX graph to visualize.
        col : str, optional
            Column in raw data to use for node coloring when `color_method='average'`.
            If None, no coloring is applied.
        pos : dict, optional
            Node positions for layout. If None, spring layout is used.
        title: str, optional
            Title for the plot. If None, no title is displayed.
        size : tuple, default=(8, 6)
            Figure size in inches.
        show_colorbar : bool, default=False
            Whether to display a colorbar (only used if col is provided).
        color_method : {"average", "community"}, default="average"
            Method for coloring nodes: by attribute average or by community.
        show_node_labels : bool, default=False
            Whether to display node labels.

        Returns
        -------
        fig : matplotlib.figure.Figure
            The created matplotlib figure.
        ax : matplotlib.axes.Axes
            The created matplotlib axes.
        """

        color_dict = None
        node_values = None
        norm = None
        node_colors = None

        # Get color values if col is provided
        if col is not None:
            color_dict, _ = self.generate_THEMAGrah_labels(
                G=G, col=col, color_method=color_method
            )
            node_values = list(color_dict.values())

        # Node sizes (default based on membership length or fallback)
        try:
            node_sizes = [
                len(G.nodes[node].get("membership", [])) * 10 for node in G.nodes
            ]
        except Exception:
            node_sizes = None

        # Colormap setup if coloring is enabled
        if node_values is not None and len(node_values) > 0:
            cmap = plt.get_cmap(
                "viridis" if color_method == "community" else "coolwarm"
            )
            norm = mcolors.Normalize(vmin=min(node_values), vmax=max(node_values))
            node_colors = [cmap(norm(color_dict[node])) for node in G.nodes]
        else:
            node_colors = "lightgray"  # default color

        # Plot setup
        fig, ax = plt.subplots(figsize=size, dpi=300)
        ax.set_frame_on(False)
        ax.set_xticks([])
        ax.set_yticks([])

        # Layout
        if pos is None:
            pos = nx.spring_layout(G, seed=12, k=0.09)

        # Draw nodes and edges
        nx.draw_networkx_nodes(
            G,
            pos,
            node_color=node_colors,
            node_size=node_sizes,
            ax=ax,
            linewidths=0.75,
            edgecolors="grey",
        )
        nx.draw_networkx_edges(
            G, pos, edgelist=G.edges, width=0.5, edge_color="grey", ax=ax
        )

        # Optional node labels
        if show_node_labels:
            nx.draw_networkx_labels(
                G,
                pos=pos,
                ax=ax,
                font_size=8,
                font_color="black",
                bbox=dict(
                    facecolor="white",
                    edgecolor="none",
                    boxstyle="round,pad=0.2",
                    alpha=0.7,
                ),
            )

        # Optional colorbar
        if show_colorbar and norm is not None:
            sm = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
            sm.set_array([])
            label = "Community" if color_method == "community" else col
            cbar = fig.colorbar(sm, ax=ax, orientation="vertical", shrink=0.7)
            cbar.set_label(label)

        plt.subplots_adjust(left=-0.3)

        if title:
            ax.set_title(title)
            ax.axis("off")

        return fig, ax

    def get_target_nodes(
        self, component, col="Percent Capacity Retiring", threshold=0.5
    ):
        """
        Identify and return nodes within a specified connected component whose average attribute value exceeds a given threshold.

        Parameters:
            component (int): Index of the connected component to analyze.
            col (str, optional): Name of the attribute in the DataFrame to evaluate for each node. Defaults to "Percent Capacity Retiring".
            threshold (float, optional): Minimum average attribute value required for a node to be included in the result. Defaults to 0.5.

        Returns:
            dict: A dictionary mapping node identifiers to their average attribute values for nodes exceeding the threshold.

        Notes:
            - Each node is expected to have a "membership" attribute, which is a list of indices referencing rows in self.raw_df.
            - If a node has no "membership" attribute or it is empty, its attribute value is considered 0.0.
        """
        comp_iter = nx.connected_components(self.G)
        components = [self.G.subgraph(nodes).copy() for nodes in comp_iter]
        subgraph = components[component]
        threshold_dict = {}
        for node in subgraph.nodes():
            memberships = subgraph.nodes[node].get("membership", [])
            if memberships:
                threshold_dict[node] = self.raw_df.loc[memberships, col].mean()
            else:
                threshold_dict[node] = 0.0
        return {node: val for node, val in threshold_dict.items() if val > threshold}

    def get_shortest_distances_to_targets(self, component, targets):
        """
        Compute the shortest distances from each node in a connected component to the nearest target node.

        Parameters
        ----------
        component : int
            The index of the connected component within the graph `self.G` to analyze.
        targets : dict
            A dictionary containing target nodes as keys. The function will compute, for each node in the specified component,
            the shortest path distance to the nearest node present in this dictionary.

        Returns
        -------
        distances : dict
            A dictionary mapping each node in the specified component to the shortest distance to any target node.
            If a node is not connected to any target, its distance will be set to float('inf').
        """
        comp_obj = nx.connected_components(self.G)
        components = [self.G.subgraph(c).copy() for c in comp_obj]
        subGraph = components[component]
        distances = {}
        for node in subGraph.nodes():
            min_dist = min(
                (
                    nx.shortest_path_length(
                        subGraph, source=node, target=target, weight="weight"
                    )
                    for target in targets
                    if nx.has_path(subGraph, node, target)
                ),
                default=float("inf"),
            )
            distances[node] = min_dist
        return distances

    def generate_THEMAGrah_labels(
        self,
        G: nx.Graph,
        col: str = "ret_STATUS",
        color_method: str = "average",
    ):
        """
        Assign colors to nodes based on either:
        - The average value of `col` for data points in each node (color_method="average"), or
        - Community membership via label propagation (color_method="community").

        Returns
        -------
        color_dict : dict
            Node -> color value (float for average, int for community ID).
        labels_dict : dictx
            Node -> label (usually the node name).
        """
        labels_dict = {node: node for node in self.G.nodes}

        if color_method == "average":
            color_dict = {
                node: self.raw_df.iloc[self.G.nodes[node]["membership"]].mean(
                    numeric_only=True
                )[col]
                for node in self.G.nodes
            }

        elif color_method == "community":
            # Detect communities and assign a 0-based integer ID to each node
            communities = list(nx.community.label_propagation_communities(G))
            community_id = {
                node: i for i, comm in enumerate(communities) for node in comm
            }
            color_dict = {node: community_id[node] for node in G.nodes}

        else:
            raise ValueError(f"Invalid color_method: {color_method}")

        return color_dict, labels_dict

    def assign_group_ids_to_rawdf(self):
        """
        Annotate the raw DataFrame with a 'Group' column indicating the connected component (group) each plant belongs to.

        Returns
        -------
        pd.DataFrame
            A copy of the raw DataFrame with an added 'Group' column.
        """
        # 1. Find connected components
        comp_obj = nx.connected_components(self.G)
        components = [self.G.subgraph(c).copy() for c in comp_obj]

        # 2. Map plant index to group number
        plant_to_group = {}
        for group_num, subgraph in enumerate(components):
            for node in subgraph.nodes:
                plant_indices = self.G.nodes[node].get("membership", [])
                for idx in plant_indices:
                    plant_to_group[idx] = group_num

        df_w_groups = self.raw_df.copy()

        # 3. Assign group number to df
        df_w_groups["Group"] = df_w_groups.index.map(plant_to_group)

        return df_w_groups

    def assign_group_ids_to_cleandf(self, df):
        """
        Annotate the raw DataFrame with a 'Group' column indicating the connected component (group) each plant belongs to.

        Returns
        -------
        pd.DataFrame
            A copy of the raw DataFrame with an added 'Group' column.
        """
        comp_obj = nx.connected_components(self.G)
        components = [self.G.subgraph(c).copy() for c in comp_obj]

        # 2. Map plant index to group number
        plant_to_group = {}
        for group_num, subgraph in enumerate(components):
            for node in subgraph.nodes:
                plant_indices = self.G.nodes[node].get("membership", [])
                for idx in plant_indices:
                    plant_to_group[idx] = group_num

        df_w_groups = df.copy()

        # 3. Assign group number to df
        df_w_groups["Group"] = df_w_groups.index.map(plant_to_group)

        return df_w_groups
