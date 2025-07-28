# Usage Guide

Welcome to the **RETIRE** usage guide! This guide will walk you through the process of using RETIRE to analyze coal plant data, explore network structures, and visualize retirement patterns. The package is designed to be accessible for environmental scientists who may be new to Python.

## Installation

First, install the RETIRE package using pip:

```bash
pip install retire
```

## Basic Usage

### The Retire Class

The main entry point to the package is the `Retire` class, which provides access to the coal plant dataset and network graph:

```python
from retire import Retire

# Initialize the Retire object
retire_obj = Retire()

# Access the coal plant dataset
df = retire_obj.raw_df
print(f"Dataset contains {len(df)} coal plants")

# Access the network graph
graph = retire_obj.graph
```

### Accessing Research Results

The `Retire` class also provides methods to access precomputed results from the research paper:

```python
# Get group analysis results
group_analysis = retire_obj.get_group_report()
print(group_analysis.head())

# Get plant-level target explanations
explanations = retire_obj.get_target_explanations()
print(explanations.head())
```

## Loading Specific Datasets

If you prefer to work directly with the datasets, you can import them individually:

```python
from retire.data import (
    load_dataset,                   # Raw coal plant dataset
    load_clean_dataset,             # Cleaned and scaled dataset
    load_projection,                # Projected retirement data
    load_generator_level_dataset,   # Generator-level details
    load_graph                      # Network graph
)

# Example: Load the raw dataset
raw_df = load_dataset()

# Example: Load the cleaned dataset
clean_df = load_clean_dataset()
```

## Visualizations with the Explore Class

The `Explore` class provides powerful visualization tools for analyzing coal plant networks and retirement patterns:

```python
from retire import Retire
from retire.explore import Explore

# Initialize the objects
retire_obj = Retire()
explore = Explore(retire_obj.graph, retire_obj.raw_df)
```

### Network Graph Visualizations

```python
# Basic network visualization colored by retirement status
fig, ax = explore.drawGraph(col="ret_STATUS",
                           show_colorbar=True,
                           color_method="average")

# Focus on a specific component (plant group)
fig, ax = explore.drawComponent(component=3,
                               col="Age",
                               show_colorbar=True,
                               title="Group 3 by Age")

# Analyze distances from target nodes
targets = explore.get_target_nodes(component=0, col="ret_STATUS", threshold=1.0)
distances = explore.get_shortest_distances_to_targets(component=0, targets=targets)
fig, ax = explore.drawPathDistance(component=0,
                                  targets=targets,
                                  distances_dict=distances,
                                  title="Distance to Retiring Plants")
```

### Statistical Visualizations

```python
# Create a heatmap showing key features across groups
from retire.examples import heatmap_config
fig, ax = explore.drawHeatMap(heatmap_config)

# Create a dot plot comparing features across groups
from retire.examples import dotplot_config
clean_df = load_clean_dataset()
fig, ax = explore.drawDotPlot(clean_df, dotplot_config)

# Create a bar chart showing plant counts by proximity group
fig, ax = explore.drawBar(title="Plant Counts by Retirement Proximity")

# Create a Sankey diagram showing plant flow between groups and retirement categories
fig, ax = explore.drawSankey()
```

### Geographic Visualizations

```python
# Create an interactive map of coal plants colored by retirement status
fig, ax = explore.drawMap()

# Create a set of maps showing plant groups and their characteristics
fig, ax = explore.drawComponentsMap()
```

## Reproducing Manuscript Figures

The `manuscript` folder contains notebooks for reproducing the figures and analyses from the research paper:

- `main.ipynb`: Core figures and analyses
- `methods.ipynb`: Methodological details and supplementary analyses
- `SI.ipynb`: Supplementary information figures

For example, to reproduce the figures from the main paper:

```python
# Navigate to the manuscript folder and open main.ipynb in Jupyter
jupyter notebook manuscript/main.ipynb
```

## Tutorials

The `tutorials` folder provides guided examples for using different parts of the package:

- `using_retire.ipynb`: Basic usage of the Retire class
- `using_explore.ipynb`: Visualization examples with the Explore class
- `using_thema.ipynb`: Working with the THEMA-generated network

To follow these tutorials, run:

```python
# Navigate to the tutorials folder and open in Jupyter
jupyter notebook tutorials/using_explore.ipynb
```

## Data Synchronization

For advanced users, the package includes scripts for synchronizing data from remote sources:

```python
# Import the sync functions
from scripts.sync_results import sync_retiredPlants_data, sync_news_data, sync_metrics_data

# Synchronize the latest retired plants data
sync_retiredPlants_data()
```

By following this guide, you can effectively use the RETIRE package to analyze coal plant data, visualize retirement patterns, and reproduce research findings even if you're new to Python.
