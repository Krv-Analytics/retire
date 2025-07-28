# Usage Guide

Welcome to the **RETIRE** usage tutorial! This guide will walk you through the process of using RETIRE to analyze coal plant data, explore network structures, and visualize retirement patterns. Follow the steps below to get started.

## Installation

First, install the RETIRE package using pip:

```bash
pip install retire
```

## Quick Start

## Loading Data

```python
from retire.data import load_dataset, load_clean_dataset, load_projection, load_graph

# Load the original coal plant dataset
raw_df = load_dataset()

# Load the cleaned and preprocessed dataset
clean_df = load_clean_dataset()

# Load the UMAP projection for visualization
projection_df = load_projection()

# Load the THEMA-generated graph
G = load_graph()
```

See the [Data Sources](data_sources.md) page for detailed information about each dataset.

## Initializing the Explorer

Create an Explore object to access visualization and analysis methods:

```python
from retire.explore import Explore

explorer = Explore(G=G, raw_df=raw_df)
```

## Basic Graph Visualization

Visualize the THEMA graph with coal plant attributes:

```python
# Visualize the graph colored by retirement status
fig, ax = explorer.drawGraph(col="ret_STATUS",
                             show_colorbar=True,
                             color_method="average")
```

## Component-Level Analysis

Focus on specific connected components for detailed analysis:

```python
# Visualize component 3 colored by plant age
fig, ax = explorer.drawComponent(component=3,
                                 col="Age",
                                 show_colorbar=True,
                                 title="Group 3 by Age")
```

## Advanced Visualizations

Create more complex visualizations to analyze patterns:

```python
# Create a heatmap of key metrics across groups
from retire.examples import heatmap_config
fig, ax = explorer.drawHeatMap(heatmap_config)

# Create a dot plot of features across groups
from retire.examples import dotplot_config
fig, ax = explorer.drawDotPlot(clean_df, dotplot_config)

# Visualize coal plants on a US map
fig, ax = explorer.drawMap()
```

## Accessing Results and Analysis

Access the precomputed results and analyses:

```python
from retire.retire import Retire

# Initialize the Retire object
retire_obj = Retire()

# Get group analysis results
group_analysis = retire_obj.get_group_report()

# Get plant-level match explanations
explanations = retire_obj.get_target_explanations()
```

With these steps, you can effectively use RETIRE to analyze coal plant data, explore retirement patterns, and reproduce the analyses from our research paper.
