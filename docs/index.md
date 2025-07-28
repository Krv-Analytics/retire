# RETIRE: Coal Plant Retirement Analysis

RETIRE is a Python package that provides tools for analyzing US coal plant retirement strategies based on contextual vulnerabilities. This package implements methods and provides data from the research paper _"Strategies to Accelerate US Coal Power Phaseout Using Contextual Retirement Vulnerabilities"_.

## Overview

The RETIRE package offers:

- **Complete US Coal Plant Dataset**: Access comprehensive data on coal plants including operational characteristics, retirement status, and contextual factors
- **Network Analysis Tools**: Explore plant relationships using similarity-based network graphs
- **Visualization Suite**: Create network graphs, geographic maps, heatmaps, and other statistical plots
- **Research Reproducibility**: Reproduce figures and analyses from the manuscript
- **Tutorial Materials**: Learn how to use the package through guided examples

## Getting Started

```python
from retire import Retire
from retire.explore import Explore

# Initialize the core objects
retire_obj = Retire()
explore = Explore(retire_obj.graph, retire_obj.raw_df)

# Access the coal plant dataset
df = retire_obj.raw_df
print(f"Dataset contains {len(df)} coal plants")

# Create a simple network visualization
fig, ax = explore.drawGraph(col='ret_STATUS', show_colorbar=True)
```

## Documentation Structure

- [**Usage Guide**](usage_guide.md): Step-by-step instructions for using the package
- [**Configuration**](configuration.md): Configuration options for analyses and visualizations
- [**Data Sources**](data_sources.md): Description of included datasets and data sources
- [**Visualization Methods**](visualization_methods.md): Details on available visualization techniques

### For Developers

- [**Data Structure**](development/data.md): Technical details about data processing
- [**Explorer Development**](development/explorer.md): Information on extending visualizations
- [**Testing**](development/testing.md): Guidelines for testing package functionality

## Citation

If you use this package in your research, please cite:

```
@article{retire2025,
  title={Strategies to Accelerate US Coal Power Phaseout Using Contextual Retirement Vulnerabilities},
  author={Sidney Gathrid\textsuperscript{*} and Jeremy Wayland\textsuperscript{*} and Stuart Wayland and Ranjit Deshmukh and Grace C. Wu},
  journal={Nature Energy},
  year={2025}
}
```

## License

This project is licensed under the BSD 3-Clause License.
