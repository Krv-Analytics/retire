```markdown
# Data Module Development

The `data` module in RETIRE provides functions for loading and processing coal plant datasets. This document outlines the key components and development considerations for working with the `data` module.

## Module Structure

The `data` module contains several functions for loading different versions of the coal plant dataset:

```python
def load_dataset():
    """Loads the US coal plants dataset from a CSV file."""
    
def load_clean_dataset():
    """Loads the cleaned and scaled US coal plant dataset."""
    
def load_projection():
    """Loads the projected US coal plant dataset."""
    
def load_graph():
    """Loads a graph from CSV files containing node and edge data."""
    
def load_generator_level_dataset():
    """Loads the generator-level US coal plants dataset."""
```

## Data Sources

The data module accesses files from the following locations:

- Raw dataset: `retire/resources/us_coal_plants_dataset.csv`
- Cleaned dataset: `retire/resources/clean_scaled_us_coalplant_dataset.csv`
- Projection: `retire/resources/projected_us_coalplant_dataset.csv`
- Graph data:
  - Nodes: `retire/resources/graph/graphnode_df.csv`
  - Edges: `retire/resources/graph/graphedge_df.csv`
- Generator-level data: `retire/resources/generator_level_dataset.csv`

## Implementation Details

### Resource Access

The module uses Python's `importlib.resources` to access package data files, ensuring compatibility across different installation methods:

```python
from importlib.resources import files

path = files("retire").joinpath("resources/us_coal_plants_dataset.csv")
```

### Graph Construction

The `load_graph()` function performs several steps to construct the graph:

1. Loads node and edge dataframes from CSV files
2. Creates a NetworkX graph object
3. Adds nodes with attributes, parsing membership information
4. Adds edges with attributes
5. Returns the complete graph

### Data Processing

The data functions handle various data cleaning and transformation tasks:

- Converting string representations to Python objects (e.g., list parsing)
- Handling missing values
- Ensuring proper data types

## Development Guidelines

When extending or modifying the `data` module, consider the following best practices:

1. **Resource Management**: Use `importlib.resources` consistently for all file access.
2. **Error Handling**: Include comprehensive error handling for file I/O and parsing operations.
3. **Documentation**: Document the structure and format of each dataset.
4. **Type Consistency**: Ensure consistent data types across related datasets.
5. **Versioning**: Consider adding version information to datasets for tracking changes.

## Example Extension

Here's an example of extending the `data` module with a new data loading function:

```python
def load_results_dataset(result_type: str = "metrics"):
    """
    Loads a specific results dataset from the resources.
    
    Parameters
    ----------
    result_type : str
        Type of results to load. Options are "metrics", "news", or "retired".
        
    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the requested results data.
        
    Raises
    ------
    ValueError
        If an invalid result_type is provided.
    """
    valid_types = ["metrics", "news", "retired"]
    if result_type not in valid_types:
        raise ValueError(f"result_type must be one of {valid_types}")
        
    path = files("retire").joinpath(f"resources/results/{result_type}.csv")
    return pd.read_csv(path)
```
```
