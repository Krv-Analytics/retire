# Explorer Development Guide

The `Explore` class in RETIRE provides a comprehensive set of visualization methods for analyzing coal plant data and network graphs. This document provides technical details for developers who want to understand, modify, or extend the visualization capabilities.

## Class Overview

The `Explore` class (`retire/explore/explore.py`) is designed to visualize and analyze relationships between coal plants using various plotting techniques. It works with both the network graph structure and the underlying coal plant data.

```python
class Explore:
    """
    Visualization and exploration class for coal plant network analysis.

    The Explore class provides comprehensive visualization tools for analyzing
    coal plant networks and retirement strategies.
    """

    def __init__(self, G: nx.Graph, raw_df: pd.DataFrame):
        """
        Initialize the Explore visualization object.

        Parameters
        ----------
        G : networkx.Graph
            Network graph of coal plants with nodes and edges representing
            plant relationships based on similarity metrics.
        raw_df : pandas.DataFrame
            Raw dataset containing coal plant information including
            characteristics, retirement status, and contextual factors.
        """
        self.G = G
        self.raw_df = raw_df
```

## Visualization Architecture

The `Explore` class organizes visualizations into several categories:

### 1. Network Graph Visualizations

These methods visualize the network structure and properties:

- **`drawGraph()`**: Visualizes the entire graph with customizable node coloring
- **`drawComponent()`**: Focuses on a specific connected component (group)
- **`drawPathDistance()`**: Shows distances from nodes to target nodes

These methods use matplotlib for static, publication-quality graph visualizations.

### 2. Statistical Visualizations

These methods create statistical representations of the data:

- **`drawHeatMap()`**: Creates heatmaps showing aggregated features across groups
- **`drawDotPlot()`**: Creates dot plots comparing features across groups, with dot size representing variance
- **`drawBar()`**: Creates stacked bar charts showing plant counts by proximity group
- **`drawSankey()`**: Creates Sankey diagrams showing flows between groups and retirement categories

These use both matplotlib (for heatmap, dot plot) and plotly (for bar charts, Sankey diagrams) to create appropriate visualizations.

### 3. Geographic Visualizations

These methods place plants on maps:

- **`drawMap()`**: Interactive US map of coal plants colored by retirement status
- **`drawComponentsMap()`**: Multiple maps faceted by component groups

These use plotly for interactive geographic visualizations.

## Core Technical Components

### Graph-Data Integration

A key design challenge addressed by the `Explore` class is integrating the graph structure (which represents clusters of plants) with the raw plant-level data. This is handled through:

1. The `membership` attribute of graph nodes, which contains indices referencing rows in the raw data
2. Helper methods like `assign_group_ids_to_rawdf()` that add group information to the data
3. Node attribute aggregation methods that compute summary statistics from member plants

### Visualization Configuration

Many visualizations accept configuration dictionaries that control their appearance and behavior:

```python
# Example configuration for heatmap
heatmap_config = {
    "aggregations": {"Age": "mean", "Total Nameplate Capacity (MW)": "mean", ...},
    "derived_columns": [{"name": "Num Plants", "formula": lambda df: df.groupby("Group").size(), ...}],
    "renaming": {"Total Nameplate Capacity (MW)": "Capacity (MW)", ...},
    "categories": {"Plant Characteristics": ["Capacity (MW)", "Age", ...], ...}
}
```

This approach allows for extensive customization while keeping method signatures clean.

### Graph Analysis Methods

Several methods perform network analysis to extract insights:

- **`get_target_nodes()`**: Identifies important nodes based on attribute thresholds
- **`get_shortest_distances_to_targets()`**: Calculates graph-theoretical distances to target nodes

These enable analyses that combine graph structure with plant characteristics.

## Implementation Details

### Graph Visualization

The core graph visualization logic is in `drawGraph_helper()`, which:

1. Determines node colors based on attributes or community structure
2. Sets node sizes based on membership count
3. Creates a layout for the nodes (defaulting to spring layout if not provided)
4. Draws nodes, edges, optional labels, and an optional colorbar

```python
def drawGraph_helper(self, G, col=None, pos=None, title=None,
                     size=(8, 6), show_colorbar=False,
                     color_method="average", show_node_labels=False):
    # Generate node colors based on attributes or community structure
    # Set node sizes based on membership counts
    # Create or use provided layout
    # Draw the graph with matplotlib
    # Add optional elements (colorbar, labels, title)
    # Return figure and axes
```

### Data Aggregation

For statistical visualizations like heatmaps, data is aggregated by group:

```python
def drawHeatMap(self, config):
    # Assign group IDs to raw data
    df = self.assign_group_ids_to_rawdf()

    # Group data and apply aggregation functions
    group_df = df.groupby("Group").agg(config["aggregations"])

    # Compute derived columns
    for col in config["derived_columns"]:
        source_df = df if col.get("input", "group") == "raw" else group_df
        group_df[col["name"]] = col["formula"](source_df)

    # Rename columns and normalize for visualization
    # Create the heatmap with annotations and category boxes
```

### Interactive Visualizations

For interactive plots like maps, the class uses plotly:

```python
def drawMap(self):
    # Prepare data for visualization
    # Create scatter_geo plot with hover information
    # Configure map appearance
    # Return the plotly figure
```

## Utility Methods

Several helper methods support the main visualization functions:

- **`generate_THEMAGrah_labels()`**: Creates node colors based on attributes or community detection
- **`assign_group_ids_to_rawdf()`**: Maps graph component membership to the raw data
- **`assign_group_ids_to_cleandf()`**: Similar, but for the cleaned dataset

## Development Guidelines

When extending or modifying the `Explore` class, follow these best practices:

### 1. Consistent Return Pattern

All visualization methods should return a tuple of `(fig, ax)`, even if `ax` is None (for plotly figures):

```python
return fig, ax  # matplotlib
# or
return fig, None  # plotly
```

### 2. Configuration Approach

For complex visualizations, use configuration dictionaries rather than numerous parameters:

```python
# Prefer this:
fig, ax = explore.drawHeatMap(config)

# Over this:
fig, ax = explore.drawHeatMap(columns=cols, aggregation=agg, colors=colors, ...)
```

### 3. Visual Styling

Maintain consistent styling across visualizations:

- Use similar color schemes where appropriate
- Apply consistent font sizes and styles
- Include meaningful titles, labels, and legends

### 4. Documentation

For each visualization method, document:

- Purpose and use cases
- Parameter descriptions and defaults
- Return values
- Example usage

### 5. Error Handling

Add robust error checking:

- Validate input parameters
- Handle missing data gracefully
- Provide informative error messages

## Extending the Explorer

### Adding a New Visualization Method

To add a new visualization method:

1. Define the method with appropriate parameters and documentation
2. Ensure it follows the established patterns (configuration, return values)
3. Add error handling and parameter validation
4. Return figure and axes objects

Example:

```python
def drawTimeSeriesAnalysis(self, time_column, value_column, by_group=False):
    """
    Visualize time series trends in coal plant data.

    Parameters
    ----------
    time_column : str
        Column name for time/date values
    value_column : str
        Column name for the values to plot over time
    by_group : bool, default=False
        Whether to separate trends by group

    Returns
    -------
    fig : matplotlib.figure.Figure
        The created matplotlib figure
    ax : matplotlib.axes.Axes
        The created matplotlib axes
    """
    # Implementation here
    return fig, ax
```

### Supporting New Data Types or Structures

If you need to add support for new data types or structures:

1. Add appropriate helper methods for integration
2. Ensure compatibility with existing methods
3. Update documentation to reflect new capabilities

### Performance Considerations

For computationally intensive visualizations:

- Consider caching intermediate results
- Optimize graph algorithms for large networks
- Implement progressive rendering for complex visualizations

## Dependencies and Requirements

The `Explore` class relies on several key libraries:

- **NetworkX**: For graph manipulation
- **Matplotlib**: For static visualizations
- **Plotly**: For interactive visualizations
- **Pandas**: For data manipulation
- **NumPy**: For numerical operations
- **Seaborn**: For statistical visualizations

Ensure all dependencies are properly specified in the package requirements.
