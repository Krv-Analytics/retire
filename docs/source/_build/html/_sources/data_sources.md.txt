# Data Sources

The RETIRE package provides access to several processed datasets:

- **Raw Coal Data**: Original US coal plants dataset with plant-level and generator-level information

  - Access via: `load_dataset()`

- **Cleaned Dataset**: Scaled, encoded, and imputed version suitable for machine learning and statistical analysis

  - Access via: `load_clean_dataset()`

- **UMAP Projection**: Low-dimensional embedding generated using UMAP for visualization and clustering

  - Access via: `load_projection()`

- **THEMA Graph**: Multiresolution, discrete graph object for community detection and network analysis

  - Access via: `load_graph()`

- **Generator Level Dataset**: Detailed dataset with generator-specific information for coal plants
  - Access via: `load_generator_level_dataset()`
