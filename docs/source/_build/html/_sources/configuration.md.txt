```markdown
# Configuration Guide

RETIRE uses YAML configuration files to customize its behavior and analysis parameters. This document explains the structure and options available in the configuration files.

## Configuration Structure

The configuration file is divided into several sections:

1. **datasets**: Paths to the data files used by RETIRE.
2. **visualizations**: Settings for controlling the appearance of plots and charts.
3. **analysis**: Parameters that control how analysis is performed.

## Example Configuration

Below is an annotated example of a RETIRE configuration file:

```yaml
# Dataset paths (optional, defaults will be used if not specified)
datasets:
  raw_data: "resources/us_coal_plants_dataset.csv"
  clean_data: "resources/clean_scaled_us_coalplant_dataset.csv"
  projection: "resources/projected_us_coalplant_dataset.csv"
  graph_nodes: "resources/graph/graphnode_df.csv"
  graph_edges: "resources/graph/graphedge_df.csv"

# Visualization preferences
visualizations:
  # Default color scheme
  colors:
    retiring: "rgb(33,102,172)"
    high_proximity: "rgb(146,197,222)"
    mid_proximity: "rgb(230, 230, 230)"
    low_proximity: "rgb(244,165,130)"
    far_from_retirement: "rgb(178,24,43)"
  
  # Graph display settings
  graph:
    node_size_factor: 10
    edge_alpha: 0.5
    colormap: "coolwarm"
    show_labels: false
  
  # Map display settings
  map:
    size_variable: "Total Nameplate Capacity (MW)"
    size_max: 13
    scope: "usa"

# Analysis parameters
analysis:
  # Proximity thresholds for categorization
  proximity_bins:
    - -Infinity
    - 0
    - 0.33
    - 0.67
    - Infinity
  
  # Key features for heatmap visualization
  heatmap_features:
    economics:
      - "Total Nameplate Capacity (MW)"
      - "Heat Rate (mmBtu/MWh)"
      - "Percent difference"
    demographics:
      - "Population density (per square mile)"
      - "Estimated percentage who somewhat/strongly oppose setting strict limits on existing coal-fire power plants"
    environmental:
      - "SO2 (tons)"
      - "NOx (tons)"
      - "CO2 (tons)"
```

## Configuration Options

### Datasets Section

The `datasets` section specifies the paths to data files:

- `raw_data`: Path to the original coal plant dataset CSV.
- `clean_data`: Path to the cleaned and scaled dataset CSV.
- `projection`: Path to the UMAP projection CSV.
- `graph_nodes`: Path to the graph nodes CSV.
- `graph_edges`: Path to the graph edges CSV.

### Visualizations Section

The `visualizations` section controls the appearance of charts and plots:

#### Colors

The `colors` subsection defines the color scheme for retirement categories:

- `retiring`: Color for plants marked as fully retiring.
- `high_proximity`: Color for plants with high proximity to retirement.
- `mid_proximity`: Color for plants with medium proximity to retirement.
- `low_proximity`: Color for plants with low proximity to retirement.
- `far_from_retirement`: Color for plants unlikely to retire soon.

#### Graph

The `graph` subsection controls graph visualization settings:

- `node_size_factor`: Multiplier for node size based on membership count.
- `edge_alpha`: Transparency of graph edges (0.0-1.0).
- `colormap`: Matplotlib colormap name for node coloring.
- `show_labels`: Boolean to control whether node labels are shown.

#### Map

The `map` subsection controls geospatial visualization settings:

- `size_variable`: Column name to use for point sizing on maps.
- `size_max`: Maximum size for points on the map.
- `scope`: Geographic scope for the map (e.g., "usa", "world").

### Analysis Section

The `analysis` section controls how analysis is performed:

#### Proximity Bins

The `proximity_bins` list defines the thresholds used to categorize plants by retirement proximity:

- Values represent cutoffs for distances in the graph.
- Must include `-Infinity` as the first value and `Infinity` as the last value.

#### Heatmap Features

The `heatmap_features` section organizes features into categories for heatmap visualization:

- Each category (e.g., `economics`, `demographics`, `environmental`) contains a list of column names.
- These categories are used for grouping and displaying boxed sections in heatmaps.

## Using Custom Configurations

To use a custom configuration file with RETIRE:

```python
from retire.config import load_config
from retire.explore import Explore

# Load custom configuration
config = load_config("path/to/config.yaml")

# Use configuration with Explore
explorer = Explore(G=G, raw_df=raw_df, config=config)
```
```
