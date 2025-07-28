# Visualization Methods

The `Explore` class in the RETIRE package provides a variety of visualization methods to help analyze and understand coal plant retirement patterns. This guide explains each visualization method, its purpose, and how to use it.

## Network Graph Visualizations

### drawGraph

Visualizes the complete network graph of coal plants with optional node coloring.

```python
fig, ax = explore.drawGraph(
    col="ret_STATUS",               # Column for node coloring
    show_colorbar=True,             # Whether to display a color bar
    color_method="average",         # Method for coloring ('average' or 'community')
    size=(10, 8),                   # Figure size (width, height) in inches
    show_node_labels=False          # Whether to display node labels
)
```

**Key Parameters:**

- `col`: Column from the raw data to use for node coloring
- `color_method`: 'average' (color by column value) or 'community' (color by graph community)
- `show_colorbar`: Whether to display a colorbar legend
- `show_node_labels`: Whether to display labels for each node

**Example Use Case:** Visualize the entire network of coal plants, colored by retirement status to identify patterns and clusters.

### drawComponent

Focuses on a specific connected component (group) of the graph.

```python
fig, ax = explore.drawComponent(
    component=3,                    # Component/group index to visualize
    col="Age",                      # Column for node coloring
    title="Group 3 - Plant Age",    # Title for the plot
    show_colorbar=True              # Whether to display a color bar
)
```

**Key Parameters:**

- `component`: Index of the connected component to visualize
- `col`: Column from the raw data to use for node coloring
- `title`: Optional title for the plot

**Example Use Case:** Examine a specific group of related plants in detail to understand their characteristics.

### drawPathDistance

Visualizes the distance from each node to the nearest target node (e.g., retiring plants).

```python
# First identify target nodes and calculate distances
targets = explore.get_target_nodes(component=0, col="ret_STATUS", threshold=1.0)
distances = explore.get_shortest_distances_to_targets(component=0, targets=targets)

# Then visualize the distances
fig, ax = explore.drawPathDistance(
    component=0,                    # Component/group index to visualize
    targets=targets,                # Dictionary of target nodes
    distances_dict=distances,       # Dictionary of distances to targets
    title="Distance to Retiring Plants",
    show_colorbar=True
)
```

**Key Parameters:**

- `component`: Index of the connected component to visualize
- `targets`: Dictionary of target node IDs (output from `get_target_nodes()`)
- `distances_dict`: Dictionary of distances from each node to nearest target (output from `get_shortest_distances_to_targets()`)

**Example Use Case:** Identify plants that are structurally similar to already-retiring plants.

## Statistical Visualizations

### drawHeatMap

Creates a heatmap showing key features across different plant groups.

```python
from retire.examples import heatmap_config

fig, ax = explore.drawHeatMap(heatmap_config)
```

**Key Parameters:**

- `config`: Dictionary containing heatmap configuration (see [Configuration Guide](configuration.md))
  - `aggregations`: How to aggregate data (e.g., mean, sum)
  - `derived_columns`: Additional columns to calculate
  - `renaming`: Column name mapping for display
  - `categories`: Grouping of columns for visual organization

**Example Use Case:** Compare multiple characteristics across different plant groups to identify patterns and contrasts.

### drawDotPlot

Creates a dot plot comparing features across groups, with dot color representing normalized value and size representing standard deviation.

```python
from retire.examples import dotplot_config
from retire.data import load_clean_dataset

clean_df = load_clean_dataset()
fig, ax = explore.drawDotPlot(clean_df, dotplot_config)
```

**Key Parameters:**

- `clean_df`: Cleaned and scaled dataset
- `config`: Dictionary containing dot plot configuration (see [Configuration Guide](configuration.md))
  - `features`: List of features to include
  - `feature_labels`: Display names for features
  - `color_map`: Colormap for the visualization
  - `dot_size_range`: Range for dot sizes (min, max)

**Example Use Case:** Compare the distribution and variability of key features across plant groups.

### drawBar

Creates a stacked bar chart showing plant counts by proximity group.

```python
fig, ax = explore.drawBar(title="Plant Counts by Retirement Proximity")
```

**Key Parameters:**

- `title`: Optional title for the chart

**Example Use Case:** Visualize the distribution of plants across different retirement proximity categories.

### drawSankey

Creates a Sankey diagram showing the flow of plants between groups and retirement categories.

```python
fig, ax = explore.drawSankey(title="Plant Flow Between Groups and Retirement Categories")
```

**Key Parameters:**

- `title`: Optional title for the diagram

**Example Use Case:** Visualize the relationship between plant groups and retirement categories.

## Geographic Visualizations

### drawMap

Creates an interactive map of US coal plants, color-coded by retirement status.

```python
fig, ax = explore.drawMap()
```

**Example Use Case:** Explore the geographic distribution of coal plants and their retirement status.

### drawComponentsMap

Creates a set of maps showing coal plants faceted by group/component.

```python
fig, ax = explore.drawComponentsMap()
```

**Example Use Case:** Compare the geographic distribution of different plant groups.

## Helper Methods

The `Explore` class also provides some helper methods for analysis:

### get_target_nodes

Identifies nodes in a component whose average attribute value exceeds a threshold.

```python
targets = explore.get_target_nodes(
    component=0,                # Component/group index
    col="ret_STATUS",           # Column to evaluate
    threshold=1.0               # Minimum average value
)
```

**Key Parameters:**

- `component`: Index of the connected component to analyze
- `col`: Column from the raw data to evaluate
- `threshold`: Minimum average value for inclusion

**Example Use Case:** Identify plants with high retirement status as targets.

### get_shortest_distances_to_targets

Calculates the shortest distances from each node to the nearest target node.

```python
distances = explore.get_shortest_distances_to_targets(
    component=0,                # Component/group index
    targets=targets             # Dictionary of target nodes
)
```

**Key Parameters:**

- `component`: Index of the connected component to analyze
- `targets`: Dictionary of target node IDs (output from `get_target_nodes()`)

**Example Use Case:** Calculate how similar each plant is to the nearest retiring plant.

## Best Practices for Visualizations

1. **Start Simple**: Begin with basic visualizations like `drawGraph` to understand the overall network structure
2. **Focus on Components**: Use `drawComponent` to examine specific plant groups in detail
3. **Compare Features**: Use `drawHeatMap` and `drawDotPlot` to compare characteristics across groups
4. **Explore Geography**: Use `drawMap` to understand geographic patterns
5. **Customize Appearance**: Adjust parameters like `color_method`, `show_colorbar`, and `size` to highlight important patterns
6. **Save Results**: All visualization methods return matplotlib figure and axes objects, which can be saved using `fig.savefig("filename.png")`

For detailed examples of these visualizations in action, see the tutorial notebooks in the `tutorials/` directory.
