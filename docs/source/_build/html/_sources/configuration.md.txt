# Configuration Guide

RETIRE uses YAML configuration files to customize visualization and analysis parameters.

## Basic Usage

To use a custom configuration file:

```python
from retire.config import load_config
from retire.explore import Explore

# Load custom configuration
config = load_config("path/to/config.yaml")

# Use configuration with Explore
explorer = Explore(G=G, raw_df=raw_df, config=config)
```

## Configuration Structure

The configuration file has three main sections:

### Visualizations

Control the appearance of plots and charts:

```yaml
visualizations:
  colors:
    retiring: "rgb(33,102,172)"
    high_proximity: "rgb(146,197,222)"
    mid_proximity: "rgb(230, 230, 230)"
    low_proximity: "rgb(244,165,130)"
    far_from_retirement: "rgb(178,24,43)"
  
  graph:
    node_size_factor: 10
    edge_alpha: 0.5
    colormap: "coolwarm"
    show_labels: false
  
  map:
    size_variable: "Total Nameplate Capacity (MW)"
    size_max: 13
    scope: "usa"
```

### Analysis Parameters

Control categorization and analysis:

```yaml
analysis:
  proximity_bins:
    - -Infinity
    - 0
    - 0.33
    - 0.67
    - Infinity
```

### Datasets (Optional)

Override default data file paths if needed:

```yaml
datasets:
  raw_data: "custom/path/to/data.csv"
  clean_data: "custom/path/to/clean_data.csv"
  # ... other dataset paths
```
