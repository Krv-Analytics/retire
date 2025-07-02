# figures/paper_figure.py

import pandas as pd
import matplotlib.pyplot as plt
from retire.data import load_graph, load_projection
from pathlib import Path
import networkx as nx


class PaperFigure:

    @staticmethod
    def generate(label: str = "graph"):
        if label == "graph":
            G = load_graph()
            pos = None
            try:
                pos = nx.spring_layout(G, seed=42)
                plt.figure(figsize=(10, 8))
                nx.draw_networkx(
                    G,
                    pos,
                    with_labels=False,
                    node_size=300,
                    node_color="skyblue",
                    edge_color="gray",
                    font_size=8,
                )
                plt.title("Main Graph Plot")
                plt.axis("off")
                plt.tight_layout()
                plt.show()
            except Exception as e:
                print("An error occurred while plotting the graph:", e)

        elif label == "projection":
            projection = load_projection()
            plt.figure(figsize=(8, 6))
            plt.scatter(
                projection["x"], projection["y"], c="skyblue", edgecolor="k", s=50
            )
            plt.xlabel("x")
            plt.ylabel("y")
            plt.title("UMAP Projection")
            plt.grid(True, linestyle="--", alpha=0.5)
            plt.tight_layout()
            plt.show()

        else:
            raise ValueError(f"Unknown label: {label}.")
