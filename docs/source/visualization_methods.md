# Visualization Methods

The `Explore` class provides comprehensive visualization capabilities for analyzing coal plant data and network structures:

## Graph Visualizations

- **`drawGraph()`**: Visualize the complete THEMA-generated NetworkX graph

  - Key parameters: `col` (coloring column), `color_method` ('average' or 'community')

- **`drawComponent()`**: Focus on a specific connected component

  - Key parameters: `component` (component index), `col` (coloring column)

- **`drawPathDistance()`**: Show shortest path distances to target nodes
  - Key parameters: `component`, `targets` (target node dict), `distances_dict`

## Statistical Visualizations

- **`drawHeatMap()`**: Generate heatmap of grouped/normalized data with category boxes

  - Key parameters: `config` (aggregations, derived columns, categories)

- **`drawDotPlot()`**: Create dot plot with color representing normalized values, size representing standard deviation
  - Key parameters: `clean_df`, `config` (features and display options)

## Flow and Distribution Charts

- **`drawBar()`**: Stacked bar chart showing plant counts by proximity group

  - Key parameters: `title` (optional chart title)

- **`drawSankey()`**: Sankey diagram showing flow between groups and retirement categories
  - Key parameters: `title` (optional diagram title)

## Geospatial Visualizations

- **`drawMap()`**: Visualize coal plants on US map with retirement status color-coding

  - No required parameters

- **`drawComponentsMap()`**: Multiple US maps faceted by component groups
  - No required parameters
