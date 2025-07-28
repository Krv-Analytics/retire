# Retire: Coal Plant Retirement Analysis

[![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

A comprehensive Python package for analyzing US coal plant retirement strategies based on contextual vulnerabilities. This package implements methods and provides data from the research paper *"Strategies to Accelerate US Coal Power Phaseout Using Contextual Retirement Vulnerabilities"* published in Nature Energy.

## 🔥 Key Features

- **📊 Rich Dataset**: Complete US coal plant data with operational characteristics, retirement status, and contextual factors
- **🕸️ Network Analysis**: Tools for analyzing plant relationships using similarity-based network graphs
- **📈 Visualization Suite**: Comprehensive plotting capabilities including network graphs, geographic maps, heatmaps, and interactive visualizations
- **🔬 Research Reproducibility**: Direct access to manuscript results and analysis outputs
- **⚡ Easy Installation**: Simple pip installation with minimal dependencies

## 🚀 Quick Start

### Installation

```bash
pip install retire
```

### Basic Usage

```python
from retire import Retire, Explore

# Initialize the analysis objects
retire_obj = Retire()
explore = Explore(retire_obj.graph, retire_obj.raw_df)

# Access the coal plant dataset
df = retire_obj.raw_df
print(f"Dataset contains {len(df)} coal plants")

# Visualize the network graph
fig, ax = explore.drawGraph(col='ret_STATUS', show_colorbar=True)

# Create an interactive geographic map
fig, ax = explore.drawMap()

# Get manuscript analysis results
group_analysis = retire_obj.get_group_report()
plant_explanations = retire_obj.get_target_explanations()
```

## 📖 Package Overview

### Main Classes

#### `Retire`
The main analysis class providing access to coal plant data and manuscript results.

```python
retire = Retire()

# Access raw coal plant dataset
df = retire.raw_df

# Access network graph
G = retire.graph

# Get group-level analysis from manuscript
groups = retire.get_group_report()

# Get plant-level targeting explanations
explanations = retire.get_target_explanations()
```

#### `Explore`
Comprehensive visualization toolkit for exploring coal plant networks and retirement patterns.

```python
explore = Explore(retire.graph, retire.raw_df)

# Network visualizations
explore.drawGraph(col='Age')                    # Color nodes by plant age
explore.drawComponent(0, col='ret_STATUS')      # Visualize specific component
explore.drawPathDistance(0, targets, distances) # Show distances to targets

# Statistical visualizations
explore.drawHeatMap(heatmap_config)             # Grouped feature heatmap
explore.drawDotPlot(clean_df, dotplot_config)   # Feature comparison plot
explore.drawBar()                               # Plant count bar chart
explore.drawSankey()                            # Flow diagram

# Geographic visualizations
explore.drawMap()                               # Interactive US map
explore.drawComponentsMap()                     # Component-wise map
```

### Data Loading Functions

```python
from retire.data import (
    load_dataset,                    # Raw coal plant dataset
    load_clean_dataset,             # Cleaned and scaled data
    load_projection,                # Projected retirement data
    load_generator_level_dataset,   # Generator-level details
    load_graph                      # Network graph
)
```

## 🎯 Use Cases

### Research & Analysis
- **Academic Research**: Reproduce and extend findings from the Nature Energy paper
- **Policy Analysis**: Understand coal plant retirement vulnerabilities and strategic targeting
- **Network Science**: Analyze plant relationships using graph-based methods

### Visualization & Communication
- **Interactive Maps**: Explore geographic patterns of coal plant retirement
- **Network Graphs**: Visualize plant clusters and relationships
- **Statistical Plots**: Compare plant characteristics across groups

### Data Access
- **Coal Plant Database**: Comprehensive dataset with operational and contextual variables
- **Retirement Tracking**: Historical and projected retirement information
- **Research Results**: Pre-computed analysis outputs from the manuscript

## 📊 Dataset Description

The package includes several interconnected datasets:

| Dataset | Description | Access Function |
|---------|-------------|-----------------|
| **Raw Coal Data** | Original US coal plants with plant and generator information | `load_dataset()` |
| **Clean Data** | Processed and scaled dataset ready for analysis | `load_clean_dataset()` |
| **Projections** | Future retirement projections and scenarios | `load_projection()` |
| **Generator Level** | Detailed generator-level operational data | `load_generator_level_dataset()` |
| **Network Graph** | Plant similarity network with nodes and edges | `load_graph()` |

### Key Variables
- **Plant Characteristics**: Capacity, age, efficiency, fuel type
- **Retirement Status**: Current retirement plans and timeline
- **Environmental**: Emissions, environmental justice metrics
- **Economic**: Operating costs, retrofit investments, market conditions  
- **Political**: Public opinion, legislative context
- **Geographic**: Location, regional energy mix

## 🎨 Visualization Examples

### Network Graph
```python
# Visualize plant network colored by retirement status
fig, ax = explore.drawGraph(
    col='ret_STATUS',
    show_colorbar=True,
    size=(12, 8)
)
```

### Geographic Map
```python
# Interactive map showing plant locations and characteristics
fig, ax = explore.drawMap()
```

### Feature Heatmap
```python
from retire.examples import heatmap_config
fig, ax = explore.drawHeatMap(heatmap_config)
```

### Dot Plot Analysis
```python
from retire.examples import dotplot_config
from retire.data import load_clean_dataset

clean_df = load_clean_dataset()
fig, ax = explore.drawDotPlot(clean_df, dotplot_config)
```

## 📚 Documentation

- **Full Documentation**: [https://retire.readthedocs.io](https://retire.readthedocs.io)
- **API Reference**: Complete function and class documentation
- **Tutorials**: Step-by-step guides and examples
- **Research Paper**: [Nature Energy Publication](https://doi.org/your-paper-doi)

## 🛠️ Development

### Setup Development Environment

```bash
git clone https://github.com/your-org/retire.git
cd retire
pip install -e ".[dev]"
```

### Building Documentation

```bash
cd docs/source
make html
```

### Running Tests

```bash
pytest tests/
```

## 📄 Citation

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

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on how to submit issues, feature requests, and pull requests.

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/your-org/retire/issues)
- **Documentation**: [Online Docs](https://retire.readthedocs.io)
- **Email**: your-email@institution.edu

## 🙏 Acknowledgments

This research was supported by [funding sources]. We thank [collaborators] for their contributions to the underlying research and dataset development.

---

**Note**: This package provides data and analysis tools for research purposes. The retirement strategies and recommendations should be considered within the broader context of energy policy, economic factors, and environmental justice considerations.