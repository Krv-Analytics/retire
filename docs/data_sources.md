# Data Sources

The RETIRE package includes several datasets that are used for analyzing coal plant retirement strategies. This document describes each dataset and explains how to access it.

## Available Datasets

- **Raw Coal Plant Data**: Original US coal plants dataset containing plant characteristics, retirement status, and contextual factors

  - Access via: `load_dataset()`

- **Cleaned Dataset**: Processed and scaled dataset ready for analysis with normalized features

  - Access via: `load_clean_dataset()`

- **Projected Dataset**: Future retirement projections and scenarios for US coal plants

  - Access via: `load_projection()`

- **Network Graph**: Plant similarity network with nodes representing plant clusters and edges representing relationships

  - Access via: `load_graph()`

- **Generator Level Data**: Detailed generator-level information for coal plants

  - Access via: `load_generator_level_dataset()`

- **Analysis Results**: Pre-computed analysis outputs from the manuscript
  - Access via: `get_group_report()`, `get_target_explanations()`

## Loading Data

You can load these datasets using functions from the `retire.data` module:

```python
from retire.data import (
    load_dataset,
    load_clean_dataset,
    load_projection,
    load_generator_level_dataset,
    load_graph
)

# Example: Load the raw dataset
raw_df = load_dataset()
```

Alternatively, you can access the raw dataset and graph directly from the `Retire` class:

```python
from retire import Retire

retire_obj = Retire()
raw_df = retire_obj.raw_df
graph = retire_obj.graph
```

## Dataset Details

### Raw Coal Plant Data (`us_coal_plants_dataset.csv`)

This dataset contains information about US coal-fired power plants, including:

- **Plant Identification**: ORIS plant codes, names, and locations
- **Physical Characteristics**: Capacity, age, heat rate, number of coal generators
- **Environmental Factors**: Emissions data (SO2, NOx, CO2), environmental justice metrics
- **Economic Context**: Operating costs, market conditions, competitiveness with renewables
- **Political Context**: Public opinion, legislative factors, utility information
- **Retirement Status**: Current retirement plans and timeline

### Cleaned Dataset (`clean_scaled_us_coalplant_dataset.csv`)

A processed version of the raw dataset with:

- Features scaled to comparable ranges
- Missing values imputed
- Categorical variables encoded
- Derived features computed

### Projected Dataset (`projected_us_coalplant_dataset.csv`)

Contains projections for coal plant retirements, including:

- Retirement probability estimates
- Timeline projections
- Scenario-based analyses

### Network Graph (`graphnode_df.csv` & `graphedge_df.csv`)

The graph structure representing relationships between coal plants:

- Nodes represent clusters of similar plants
- Edges represent relationships based on similarity metrics
- Node attributes include membership lists linking to the original dataset
- Edge attributes include weights representing similarity strength

### Generator Level Dataset (`generator_level_dataset.csv`)

More granular data at the generator level (rather than plant level):

- Unit-specific characteristics
- Operational data for individual generators
- Technical specifications

### Analysis Results (`results/`)

Pre-computed results from the research paper:

- `group_analysis.csv`: Analysis of plant groups with similar characteristics
- `plant_level_match_explanations.csv`: Detailed explanations for targeting specific plants
- `metrics.csv`: Quantitative metrics used in the analysis
- `retired.csv`: Data on retired plants
- `news.csv`: News and announcements related to coal plant retirements

## Data Location

All datasets are stored in the `retire/resources/` directory within the package. The exact paths are:

```
retire/resources/
├── clean_scaled_us_coalplant_dataset.csv
├── generator_level_dataset.csv
├── projected_us_coalplant_dataset.csv
├── us_coal_plants_dataset.csv
├── graph/
│   ├── graphedge_df.csv
│   └── graphnode_df.csv
└── results/
    ├── group_analysis.csv
    ├── metrics.csv
    ├── news.csv
    ├── plant_level_match_explanations.csv
    └── retired.csv
```
