# Development & Testing

## Running Tests

RETIRE uses pytest for testing. To run tests:

```bash
pytest
```

## Contributing

When contributing to RETIRE:

1. **Test Coverage**: Write tests for new functionality
2. **Documentation**: Update docs for API changes  
3. **Code Style**: Follow existing patterns and conventions

## Example Test

```python
import pytest
import pandas as pd
from retire.data import load_dataset

def test_load_dataset_structure():
    """Test that load_dataset returns a DataFrame with expected structure."""
    df = load_dataset()
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
```
