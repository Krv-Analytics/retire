# figures/coal_figure.py

import numpy as np
import pandas as pd
import seaborn as sns
import networkx as nx
from typing import Dict
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.colors import Normalize


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
        targets,
        distances_dict,
        col="Percent Capacity Retiring",
        title="",
        seed=5,
        show_colorbar=True,
        size_by_degree=True,
        scaled_legend=False,
        vmax=2.5,
        figsize=(10, 4),
    ):
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

    # ╭────────────────────────────────╮
    # │   Helper Functions             |
    # ╰────────────────────────────────╯

    def compute_retirement_by_node(self, component, col="Percent Capacity Retiring"):
        """
        For each node in the graph, calculate the average retirement percent
        from the associated plants (via membership indices).
        """
        comp_obj = nx.connected_components(self.G)
        components = [self.G.subgraph(c).copy() for c in comp_obj]
        subGraph = components[component]
        percent_retiring = {}
        for node in subGraph.nodes():
            indices = subGraph.nodes[node].get("membership", [])
            if indices:
                percent_retiring[node] = self.raw_df.loc[indices, col].mean()
            else:
                percent_retiring[node] = 0.0
        return percent_retiring

    def get_key_nodes(self, percent_retiring_dict, threshold=0.5):
        """
        Return nodes with retirement percent above a threshold.
        """
        return {
            node: val for node, val in percent_retiring_dict.items() if val > threshold
        }

    def get_shortest_distances_to_targets(self, component, targets):
        """
        For each node in G, compute the distance to the nearest target node.
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
