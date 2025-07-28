# Testing Guidelines

This document outlines the recommended testing approach for the RETIRE package. While the V0 release is still in development and a complete test suite has not yet been implemented, this guide provides a framework for developing tests as the package matures.

## Testing Framework

We recommend using pytest for testing the RETIRE package. Tests should be organized in a `tests` directory that mirrors the structure of the source code.

## Recommended Test Structure

The tests should be organized into modules corresponding to the package structure:

```
tests/
├── __init__.py
├── test_retire.py        # Tests for the main Retire class
├── data/
│   ├── __init__.py
│   └── test_data.py      # Tests for data loading functions
├── explore/
│   ├── __init__.py
│   └── test_explore.py   # Tests for exploration and visualization
└── utils/
    ├── __init__.py
    └── test_utils.py     # Tests for utility functions
```

## Running Tests

Once tests are implemented, they can be run from the root directory:

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_retire.py

# Run with coverage report
pytest --cov=retire tests/
```

## Test Development Guidelines

When writing tests for RETIRE, follow these guidelines:

### 1. Isolate External Dependencies

Use fixtures or mocks to isolate tests from external dependencies:

```python
import pytest
import pandas as pd
import networkx as nx

@pytest.fixture
def sample_graph():
    """Create a small test graph."""
    G = nx.Graph()
    G.add_node("A", membership=[0, 1])
    G.add_node("B", membership=[2, 3])
    G.add_edge("A", "B", weight=0.5)
    return G

@pytest.fixture
def sample_dataframe():
    """Create a small test dataframe."""
    return pd.DataFrame({
        "ORISPL": [1001, 1002, 1003, 1004],
        "Plant Name": ["Plant A", "Plant B", "Plant C", "Plant D"],
        "Age": [40, 35, 50, 25],
        "ret_STATUS": [0, 1, 2, 0]
    })

def test_explore_init(sample_graph, sample_dataframe):
    """Test Explore class initialization."""
    from retire.explore import Explore
    explore = Explore(sample_graph, sample_dataframe)
    assert explore.G == sample_graph
    assert explore.raw_df.equals(sample_dataframe)
```

### 2. Test Different Aspects of Functionality

Include tests for different aspects of each module:

1. **Functional Tests**: Verify that functions and methods work correctly
2. **Parameter Tests**: Check that different parameter combinations work as expected
3. **Edge Case Tests**: Test boundary conditions and special cases
4. **Error Handling Tests**: Verify that errors are raised and handled appropriately

### 3. Test Visualization Outputs

For visualization functions, test that they produce the expected outputs:

```python
def test_draw_graph_output(sample_graph, sample_dataframe):
    """Test that drawGraph produces a figure and axes."""
    from retire.explore import Explore
    explore = Explore(sample_graph, sample_dataframe)
    fig, ax = explore.drawGraph()
    assert fig is not None
    assert ax is not None
    # Check basic properties of the visualization
    assert len(ax.collections) > 0  # Should have drawn something
```

### 4. Test Data Loading and Processing

Ensure that data loading functions handle different scenarios correctly:

```python
def test_load_dataset_structure():
    """Test that load_dataset returns a DataFrame with the expected structure."""
    from retire.data import load_dataset
    df = load_dataset()

    # Check that it's a DataFrame
    assert isinstance(df, pd.DataFrame)

    # Check that it has the expected columns
    expected_columns = ['ORISPL', 'Plant Name', 'LAT', 'LON', 'ret_STATUS']
    for col in expected_columns:
        assert col in df.columns

    # Check that it has data
    assert len(df) > 0
```

### 5. Test Helper Functions

Test utility and helper functions that support the main functionality:

```python
def test_get_target_nodes(sample_graph, sample_dataframe):
    """Test the get_target_nodes method."""
    from retire.explore import Explore
    explore = Explore(sample_graph, sample_dataframe)

    # Mock the connected components to return our sample graph
    explore.G = nx.Graph()
    explore.G.add_nodes_from(sample_graph.nodes(data=True))
    explore.G.add_edges_from(sample_graph.edges(data=True))

    targets = explore.get_target_nodes(component=0, col="ret_STATUS", threshold=0.5)
    assert isinstance(targets, dict)
    # Check target nodes based on our sample data
```

## Example Full Test File

Here's an example of what a complete test file for the `data` module might look like:

```python
import pytest
import pandas as pd
import networkx as nx
import os
from importlib.resources import files
from unittest import mock

from retire.data import (
    load_dataset,
    load_clean_dataset,
    load_graph,
    load_projection,
    load_generator_level_dataset
)

# Mock file paths for testing
@pytest.fixture
def mock_csv_path():
    return mock.patch("importlib.resources.files", return_value=mock.MagicMock(
        joinpath=mock.MagicMock(return_value="mock_path.csv")
    ))

@pytest.fixture
def mock_read_csv():
    return mock.patch("pandas.read_csv", return_value=pd.DataFrame({
        "ORISPL": [1001, 1002],
        "Plant Name": ["Test Plant A", "Test Plant B"],
        "ret_STATUS": [0, 1]
    }))

def test_load_dataset(mock_csv_path, mock_read_csv):
    """Test that load_dataset calls the correct path and returns a DataFrame."""
    with mock_csv_path, mock_read_csv as mocked_read:
        df = load_dataset()

        # Check that read_csv was called with the right path
        mocked_read.assert_called_once_with("mock_path.csv")

        # Check that a DataFrame is returned with expected columns
        assert isinstance(df, pd.DataFrame)
        assert "ORISPL" in df.columns
        assert "Plant Name" in df.columns

def test_load_graph(mock_csv_path):
    """Test that load_graph correctly builds a graph from node and edge dataframes."""
    # Create mock dataframes for nodes and edges
    node_df = pd.DataFrame({
        "node": ["A", "B"],
        "membership": ["[0]", "[1]"]
    })
    edge_df = pd.DataFrame({
        "source": ["A"],
        "target": ["B"],
        "weight": [0.5]
    })

    # Mock reading the CSV files to return our test dataframes
    with mock_csv_path:
        with mock.patch("pandas.read_csv", side_effect=[node_df, edge_df]):
            G = load_graph()

            # Check graph properties
            assert isinstance(G, nx.Graph)
            assert list(G.nodes()) == ["A", "B"]
            assert list(G.edges()) == [("A", "B")]
            assert G.edges[("A", "B")]["weight"] == 0.5
```

## Integration with CI/CD

As the project matures, tests should be integrated into a continuous integration workflow:

1. Run tests automatically on pull requests
2. Generate coverage reports
3. Enforce minimum test coverage thresholds
4. Check for code quality and style issues

## Test Data Management

For tests requiring larger datasets:

1. Create small, representative test datasets
2. Store test data separately from production data
3. Use fixtures to load and manage test data
4. Consider parameterized tests for testing with different data inputs

## Conclusion

While the test suite is still under development for RETIRE V0, following these guidelines will help ensure that as tests are added, they provide effective coverage and verification of the package's functionality.
