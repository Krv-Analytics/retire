# Data Module Development

The `data` module in RETIRE provides functions for loading and processing coal plant datasets for analysis. This document outlines the key components and development considerations for those working on extending or modifying the data module.

## Module Structure

The `data` module (`retire/data/data.py`) contains several functions for loading different versions of the coal plant dataset:

```python
def load_dataset():
    """
    Loads the US coal plants dataset from a CSV file.

    Returns:
        pandas.DataFrame: A DataFrame containing the data from 'us_coal_plants_dataset.csv'.
    """

def load_clean_dataset():
    """
    Loads the cleaned and scaled US coal plant dataset from a CSV file.

    Returns:
        pandas.DataFrame: A DataFrame containing the cleaned and scaled US coal plant data.
    """

def load_projection():
    """
    Loads the projected US coal plant dataset from a CSV file.

    Returns:
        pandas.DataFrame: A DataFrame containing the projected US coal plant data.
    """

def load_graph():
    """
    Loads a graph from CSV files containing node and edge data.

    Returns:
        networkx.Graph: A graph object with nodes and edges populated from the CSV files.
    """

def load_generator_level_dataset():
    """
    Loads the generator-level US coal plants dataset from a CSV file.

    Returns:
        pandas.DataFrame: A DataFrame containing the generator-level data.
    """
```

## Data Files and Organization

The data module accesses files from the following locations within the package:

- **Raw dataset**: `retire/resources/us_coal_plants_dataset.csv`
  - Contains all coal plants with their characteristics, retirement status, and contextual factors
- **Cleaned dataset**: `retire/resources/clean_scaled_us_coalplant_dataset.csv`
  - Processed version with normalized features, ready for analysis
- **Projected dataset**: `retire/resources/projected_us_coalplant_dataset.csv`
  - Contains future retirement projections and scenarios
- **Graph data**:
  - **Nodes**: `retire/resources/graph/graphnode_df.csv`
  - **Edges**: `retire/resources/graph/graphedge_df.csv`
  - Together represent the network structure of plant relationships
- **Generator-level data**: `retire/resources/generator_level_dataset.csv`
  - More granular data at the individual generator level
- **Analysis results**:
  - `retire/resources/results/group_analysis.csv`
  - `retire/resources/results/plant_level_match_explanations.csv`
  - `retire/resources/results/metrics.csv`
  - `retire/resources/results/news.csv`
  - `retire/resources/results/retired.csv`

## Implementation Details

### Resource Access Pattern

The module uses Python's `importlib.resources` to access package data files, ensuring compatibility across different installation methods and environments:

```python
from importlib.resources import files

path = files("retire").joinpath("resources/us_coal_plants_dataset.csv")
return pd.read_csv(path)
```

This approach is preferred over hardcoding paths as it works regardless of how the package is installed (pip, development mode, etc.).

### Graph Construction

The `load_graph()` function performs several steps to construct the network graph:

1. Loads node and edge dataframes from CSV files
2. Creates a NetworkX graph object
3. Adds nodes with attributes, handling special parsing for the "membership" field
4. Adds edges with attributes
5. Returns the complete graph

The membership attribute of each node is particularly important as it contains the indices of plants in the raw dataset that belong to that node.

### Data Synchronization

The `scripts/sync_results.py` module provides functions to synchronize data from external sources:

```python
def sync_retiredPlants_data():
    """Synchronizes retired plants data from an external source."""

def sync_news_data():
    """Synchronizes news data from an external source."""

def sync_metrics_data():
    """Synchronizes metrics data from an external source."""
```

These functions read data from external CSV files (configured in `scripts/config.py`) and update the corresponding files in the package resources.

## Dataset Details

### Raw Coal Plant Dataset

The primary dataset contains the following key columns:

- **Plant identification**: `ORISPL`, `Plant Name`, etc.
- **Physical characteristics**: `Total Nameplate Capacity (MW)`, `Age`, `Heat Rate (mmBtu/MWh)`, etc.
- **Environmental factors**: `SO2 (tons)`, `NOx (tons)`, `CO2 (tons)`, etc.
- **Economic context**: Operating costs, market indicators
- **Political context**: Public opinion metrics, legislative factors
- **Retirement status**: `ret_STATUS`, `Retirement Date`, etc.

### Network Graph Structure

The network graph represents relationships between coal plants:

- **Nodes**: Represent clusters of similar plants
- **Node attributes**:
  - `membership`: List of indices linking to plants in the raw dataset
  - Other attributes derived from member plants
- **Edges**: Connect related plant clusters
- **Edge attributes**:
  - `weight`: Similarity strength between nodes
  - Other relationship metrics

## Development Guidelines

When extending or modifying the `data` module, follow these best practices:

1. **Resource Management**:

   - Use `importlib.resources` consistently for all file access
   - Avoid hardcoded paths

2. **Error Handling**:

   - Include comprehensive error handling for file I/O operations
   - Provide informative error messages for missing files or parsing issues

3. **Documentation**:

   - Document the structure and format of each dataset
   - Include descriptions of key columns and their significance
   - Use NumPy-style docstrings for function documentation

4. **Type Consistency**:

   - Ensure consistent data types across related datasets
   - Handle type conversions explicitly where needed

5. **Data Integrity**:
   - Add validation checks for critical data fields
   - Ensure node membership lists correctly reference the raw dataset

## Extending the Data Module

### Adding a New Data Source

To add a new data source:

1. Add the data file to `retire/resources/` (or appropriate subdirectory)
2. Create a loading function following the established pattern:

```python
def load_new_dataset():
    """
    Loads a new dataset from resources.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the new dataset.
    """
    path = files("retire").joinpath("resources/path_to_new_data.csv")
    return pd.read_csv(path)
```

3. Update the `__init__.py` file to expose the new function
4. Add appropriate documentation for the new dataset

### Adding Results Data

To add a new type of results data:

1. Add the results file to `retire/resources/results/`
2. Add a method to the `Retire` class to access the results:

```python
def get_new_results(self):
    """
    Load a new type of results data.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the new results data.
    """
    path = files("retire").joinpath("resources/results/new_results.csv")
    return pd.read_csv(path)
```

3. Update the synchronization scripts if the results should be updated from external sources

## Data Processing and Transformation

While the current implementation focuses on data loading, future developments might include more sophisticated data processing:

- Feature engineering
- Data cleaning and normalization
- Time series analysis for retirement projections
- Geospatial data processing

These capabilities should be implemented as separate functions with clear documentation of their transformations and dependencies.
