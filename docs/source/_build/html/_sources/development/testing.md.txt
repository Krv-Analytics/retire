```markdown
# Testing

This document outlines the testing approach and structure for the RETIRE package.

## Testing Framework

RETIRE uses pytest for testing. The test files are organized in the `tests` directory and follow the same structure as the source code.

## Running Tests

To run the tests, navigate to the root directory of the project and run:

```bash
pytest
```

## Test Structure

The tests are organized into separate modules corresponding to the package structure:

- `tests/imputation/`: Tests for data imputation functionality
- `tests/magic/`: Tests for auxiliary operations and utilities
- `tests/phil/`: Tests for the core algorithms and models

## Writing Tests

When writing tests for RETIRE, follow these guidelines:

1. **Test Naming**: Name tests with a `test_` prefix and a descriptive name.
2. **Fixtures**: Use pytest fixtures for setup and teardown.
3. **Assertions**: Use specific assertions that provide useful error messages.
4. **Data**: Use small, representative datasets for testing.
5. **Coverage**: Aim for high test coverage of critical functionality.

## Example Test

Here's an example test for the `load_dataset` function:

```python
import pytest
import pandas as pd
from retire.data import load_dataset

def test_load_dataset_structure():
    """Test that load_dataset returns a DataFrame with the expected structure."""
    df = load_dataset()
    
    # Check that it's a DataFrame
    assert isinstance(df, pd.DataFrame)
    
    # Check that it has the expected columns
    expected_columns = ['ORISPL', 'Plant Name', 'LAT', 'LON', 'Age', 'ret_STATUS']
    for col in expected_columns:
        assert col in df.columns
    
    # Check that it has data
    assert len(df) > 0
```
```
