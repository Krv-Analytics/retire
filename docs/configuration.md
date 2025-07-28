# Configuration Guide

RETIRE uses configuration dictionaries to customize its visualizations and analyses. This guide explains how to use these configurations with the provided example files.

## Configuration Types

The RETIRE package includes two main types of configuration:

1. **Heatmap Configuration**: Controls the appearance and data selection for heatmap visualizations
2. **Dotplot Configuration**: Controls the appearance and data selection for dot plot visualizations

These configurations are provided as example Python dictionaries in the `retire.examples` module.

## Example Usage

### Heatmap Configuration

The heatmap configuration controls how group-level features are visualized in a heatmap:

```python
from retire import Retire
from retire.explore import Explore
from retire.examples import heatmap_config

# Initialize objects
retire_obj = Retire()
explore = Explore(retire_obj.graph, retire_obj.raw_df)

# Create heatmap with the provided configuration
fig, ax = explore.drawHeatMap(heatmap_config)
```

### Dot Plot Configuration

The dot plot configuration controls how features are compared across groups:

```python
from retire import Retire
from retire.explore import Explore
from retire.examples import dotplot_config
from retire.data import load_clean_dataset

# Initialize objects
retire_obj = Retire()
explore = Explore(retire_obj.graph, retire_obj.raw_df)
clean_df = load_clean_dataset()

# Create dot plot with the provided configuration
fig, ax = explore.drawDotPlot(clean_df, dotplot_config)
```

## Heatmap Configuration Structure

The heatmap configuration is a dictionary with the following structure:

```python
heatmap_config = {
    # Aggregation functions for grouping
    "aggregations": {
        "Total Nameplate Capacity (MW)": "mean",
        "Age": "mean",
        "Heat Rate (mmBtu/MWh)": "mean",
        # More columns and aggregation functions...
    },

    # Derived columns (calculated during visualization)
    "derived_columns": [
        {
            "name": "Num Plants",
            "formula": lambda df: df.groupby("Group").size(),
            "input": "raw"
        },
        # More derived columns...
    ],

    # Column name mapping for display
    "renaming": {
        "Total Nameplate Capacity (MW)": "Capacity (MW)",
        "Heat Rate (mmBtu/MWh)": "Heat Rate",
        # More column renamings...
    },

    # Categories for visual grouping in the heatmap
    "categories": {
        "Plant Characteristics": [
            "Capacity (MW)",
            "Age",
            # More columns...
        ],
        "Environmental": [
            "SO2 (tons)",
            "NOx (tons)",
            # More columns...
        ],
        # More categories...
    }
}
```

### Key Heatmap Configuration Elements

- **aggregations**: Specifies how to aggregate plant-level data for each group (e.g., mean, median, sum)
- **derived_columns**: Creates new columns calculated from the data
- **renaming**: Maps original column names to more readable display names
- **categories**: Organizes columns into logical groups for the heatmap visualization

## Dot Plot Configuration Structure

The dot plot configuration is a dictionary with the following structure:

```python
dotplot_config = {
    # List of features to include in the dot plot
    "features": [
        "Total Nameplate Capacity (MW)",
        "Heat Rate (mmBtu/MWh)",
        "Age",
        # More features...
    ],

    # Mapping of feature names to display labels
    "feature_labels": {
        "Total Nameplate Capacity (MW)": "Capacity (MW)",
        "Heat Rate (mmBtu/MWh)": "Heat Rate",
        # More label mappings...
    },

    # Color map for visualization
    "color_map": "coolwarm",

    # Range for dot sizes (min, max)
    "dot_size_range": (10, 650),

    # Function to normalize feature values
    "normalize_feature": lambda s: (s - s.min()) / (s.max() - s.min())
}
```

### Key Dot Plot Configuration Elements

- **features**: List of columns to include in the visualization
- **feature_labels**: Maps original column names to more readable display labels
- **color_map**: Matplotlib colormap name for the color scale
- **dot_size_range**: Tuple defining minimum and maximum dot sizes
- **normalize_feature**: Function to normalize values for color mapping

## Creating Custom Configurations

You can create your own custom configurations by modifying the example configurations:

```python
from retire.examples import heatmap_config
import copy

# Create a copy of the default configuration
my_heatmap_config = copy.deepcopy(heatmap_config)

# Modify the configuration
my_heatmap_config["categories"]["Economic"] = [
    "Capacity (MW)",
    "Heat Rate",
    "Percent difference"
]

# Use your custom configuration
fig, ax = explore.drawHeatMap(my_heatmap_config)
```

## Example Configuration File

The package also includes an example YAML configuration file (`config_example.yaml`) that demonstrates how configuration might be structured for future versions of the package. This file is primarily for reference and is not currently used by the code in the V0 release.

```yaml
# Example configuration file for RETIRE analysis
datasets:
  raw_data: "resources/us_coal_plants_dataset.csv"
  clean_data: "resources/clean_scaled_us_coalplant_dataset.csv"

visualizations:
  colors:
    retiring: "rgb(33,102,172)"
    high_proximity: "rgb(146,197,222)"

  graph:
    node_size_factor: 10
    edge_alpha: 0.5

  map:
    size_variable: "Total Nameplate Capacity (MW)"
    size_max: 13

analysis:
  proximity_bins:
    - -Infinity
    - 0
    - 0.33
    - 0.67
    - Infinity

  heatmap_features:
    economics:
      - "Total Nameplate Capacity (MW)"
      - "Heat Rate (mmBtu/MWh)"
```

The example YAML configuration demonstrates how various aspects of the analysis and visualization process could be configured in future releases.
