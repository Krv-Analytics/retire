# figures/coal_figure.py

import numpy as np
import pandas as pd
import seaborn as sns
import networkx as nx
from typing import Dict
from matplotlib import rcParams
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as patches
from matplotlib.colors import Normalize
from sklearn.preprocessing import StandardScaler


class CoalFigure:

    def __init__(self, G: nx.Graph, raw_df: pd.DataFrame):
        self.G = G
        self.raw_df = raw_df

    def drawGraph(
        self,
        col: str = "ret_STATUS",
        pos: Dict[str, np.ndarray] = None,
        size: tuple = (8, 6),
        show_colorbar: bool = False,
        color_method: str = "average",
        show_node_labels: bool = False,
    ):
        """
        Visualize a THEMA generated NetworkX graph with nodes colored by a specified attribute or community assignment.

        Parameters
        ----------
        col : str
            Column in raw data to use for node coloring when `color_method='average'`.
        pos : dict, optional
            Node positions for layout. If None, spring layout is used.
        size : tuple, default=(8, 6)
            Figure size in inches.
        show_colorbar : bool, default=False
            Whether to display a colorbar.
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
        # Compute node values and sizes
        color_dict, _ = self.generate_THEMAGrah_labels(
            col=col, color_method=color_method
        )
        node_values = list(color_dict.values())
        node_sizes = [
            len(self.G.nodes[node]["membership"]) * 10 for node in self.G.nodes
        ]

        # Choose colormap
        cmap = plt.colormaps.get_cmap(
            "viridis" if color_method == "community" else "coolwarm"
        )

        # Normalize color values
        norm = mcolors.Normalize(vmin=min(node_values), vmax=max(node_values))
        node_colors = [cmap(norm(color_dict[node])) for node in self.G.nodes]

        # Create plot
        fig, ax = plt.subplots(figsize=size, dpi=300)
        ax.set_frame_on(False)
        ax.set_xticks([])
        ax.set_yticks([])

        # Node positions
        if pos is None:
            pos = nx.spring_layout(self.G, seed=12, k=0.09)

        # Draw graph
        nx.draw_networkx_nodes(
            self.G,
            pos,
            node_color=node_colors,
            node_size=node_sizes,
            ax=ax,
            linewidths=0.75,
            edgecolors="grey",
        )
        nx.draw_networkx_edges(
            self.G, pos, edgelist=self.G.edges, width=0.5, edge_color="grey", ax=ax
        )

        if show_node_labels:
            nx.draw_networkx_labels(
                self.G,
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
        if show_colorbar:
            sm = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
            sm.set_array([])
            label = "Community" if color_method == "community" else col
            cbar = fig.colorbar(sm, ax=ax, orientation="vertical", shrink=0.7)
            cbar.set_label(label)

        plt.subplots_adjust(left=-0.3)

        return fig, ax

    def drawComponet(
        self,
        component: int,
        col: str = "ret_STATUS",
        pos: Dict[str, np.ndarray] = None,
        size: tuple = (8, 6),
        show_colorbar: bool = False,
        color_method: str = "average",
        show_node_labels: bool = False,
    ):
        """
        Draws a specific connected component of the graph.

        Parameters:
            component (int): Index of the connected component to draw.
            col (str, optional): Node attribute to use for coloring. Defaults to "ret_STATUS".
            pos (Dict[str, np.ndarray], optional): Dictionary specifying node positions. If None, positions are determined automatically.
            size (tuple, optional): Size of the figure as (width, height). Defaults to (8, 6).
            show_colorbar (bool, optional): Whether to display a colorbar. Defaults to False.
            color_method (str, optional): Method for determining node colors. Defaults to "average".
            show_node_labels (bool, optional): Whether to display node labels. Defaults to False.

        Returns:
            tuple: Matplotlib figure and axes objects (fig, ax) for the drawn component.
        """
        comp_obj = nx.connected_components(self.G)
        components = [self.G.subgraph(c).copy() for c in comp_obj]
        subGraph = components[component]
        # Use subGraph for drawing
        fig, ax = self.drawGraph(
            col=col,
            pos=pos,
            size=size,
            show_colorbar=show_colorbar,
            color_method=color_method,
            show_node_labels=show_node_labels,
        )

        return fig, ax

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
                "S",
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

    # ╭────────────────────────────────╮
    # │   Helper Functions             |
    # ╰────────────────────────────────╯

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
        labels_dict : dict
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
            communities = list(nx.community.label_propagation_communities(self.G))
            community_id = {
                node: i for i, comm in enumerate(communities) for node in comm
            }
            color_dict = {node: community_id[node] for node in self.G.nodes}

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
