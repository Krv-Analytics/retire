# Retire: Coal Plant Retirement Analysis

[![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Development Status](https://img.shields.io/badge/status-v0%20WIP-orange.svg)](https://github.com/your-org/retire)

> **⚠️ Work in Progress**: This is a v0 release. Features and APIs may change.

A Python package for US coal plant retirement analysis based on research published in _Nature Energy_. Provides data and analysis tools for understanding coal plant retirement strategies using contextual vulnerabilities.

## Key Features

- **Comprehensive Dataset**: Detailed coal plant data with operational and contextual factors
- **Network Analysis**: Analyze plant relationships using similarity metrics
- **Visualization Suite**: Rich plotting capabilities for retirement patterns
- **Research Reproducibility**: Access to manuscript results and analysis

## Quick Start

### Installation

```bash
git clone https://github.com/Krv-Analytics/retire.git
cd retire
pip install uv
uv sync
```

> **Note**: This package will soon be available as a pip-installable package.

```bash
pip install retire
```

### Basic Usage

```python
from retire import Retire, Explore

# Load data and create analysis objects
retire_obj = Retire()
explore = Explore(retire_obj.graph, retire_obj.raw_df)

# Visualize the network
fig, ax = explore.drawGraph(col='ret_STATUS')

# Create geographic map
fig, ax = explore.drawMap()

# Get manuscript results
group_analysis = retire_obj.get_group_report()
explanations = retire_obj.get_target_explanations()
```

## Documentation

See the [full documentation](docs/) for detailed usage instructions:

- [Usage Guide](docs/source/usage_guide.md) - Step-by-step tutorial
- [Data Sources](docs/source/data_sources.md) - Available datasets
- [Visualization Methods](docs/source/visualization_methods.md) - Plotting capabilities
- [Configuration](docs/source/configuration.md) - Customization options

## API Overview

### Main Classes

**`Retire`** - Main analysis class with data access and manuscript results
**`Explore`** - Visualization toolkit for networks and geographic data

### Data Loading

```python
from retire.data import load_dataset, load_clean_dataset, load_projection, load_graph
```

## Development

### Running Tests

```bash
pytest
```

### Contributing

This is a v0 WIP release. When contributing:

1. **Test Coverage**: Write tests for new functionality
2. **Documentation**: Update docs for API changes
3. **Code Style**: Follow existing patterns and conventions

## License

This project is licensed under the BSD 3-Clause License - see the [LICENSE.md](LICENSE.md) file for details.

## Citation

If you use this package in your research, please cite:

```bibtex
@article{retire2025,
  title={Strategies to Accelerate US Coal Power Phaseout Using Contextual Retirement Vulnerabilities},
  author={Your Name and Co-authors},
  journal={Nature Energy},
  year={2025},
  doi={10.1038/your-doi}
}
```

---

**Note**: This package provides data and analysis tools for research purposes. Retirement strategies should be considered within broader energy policy and environmental justice contexts.
