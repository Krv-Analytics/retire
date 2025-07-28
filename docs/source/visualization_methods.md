# Visualization Methods

-----------------------------------------------------------------------------------
Method                    Description                         Configuration Options
-----------------------------------------------------------------------------------|
                       |                                    |                      |
drawGraph              | Visualize a THEMA-generated       | - col: Column for    |
                       | NetworkX graph with optional node  |   node coloring      |
                       | coloring based on attributes or    | - pos: Node positions|
                       | community structure                | - color_method:      |
                       |                                    |   'average' or       |
                       |                                    |   'community'        |
------------------------------------------------------------------------------------
                       |                                    |                      |
drawComponent          | Draws a specific connected        | - component: Index of|
                       | component of the graph with        |   the component      |
                       | customizable node coloring         | - col: Column for    |
                       | and appearance                     |   node coloring      |
                       |                                    | - color_method: Same |
                       |                                    |   as drawGraph       |
-------------------------------------------------------------------------------------
                       |                                    |                      |
drawPathDistance       | Visualizes shortest path          | - component: Index   |
                       | distances from all nodes to a      |   of the component   |
                       | set of target nodes within a       | - targets: Dict of   |
                       | specified connected component      |   target node IDs    |
                       |                                    | - distances_dict:    |
                       |                                    |   Node distances     |
---------------------------------------------------------------------------------------
                       |                                    |                      |
drawHeatMap            | Generates a heatmap visualization | - config: Dict with  |
                       | of grouped and normalized data     |   aggregations,      |
                       | with annotated values and          |   derived columns,   |
                       | category boxes                     |   renaming, and      |
                       |                                    |   categories         |
---------------------------------------------------------------------------------------
                       |                                    |                      |
drawDotPlot            | Creates a dot plot visualizing    | - clean_df: Cleaned  |
                       | feature values across groups,      |   DataFrame          |
                       | with dot color representing        | - config: Dict with  |
                       | normalized values and dot size     |   features and       |
                       | representing standard deviation    |   display options    |
---------------------------------------------------------------------------------------
                       |                                    |                      |
drawBar                | Generates stacked bar chart       | - title: Optional    |
                       | showing plant counts by proximity  |   chart title        |
                       | group                              |                      |
---------------------------------------------------------------------------------------
                       |                                    |                      |
drawSankey             | Creates a Sankey diagram showing  | - title: Optional    |
                       | flow between groups and            |   diagram title      |
                       | retirement categories              |                      |
---------------------------------------------------------------------------------------
                       |                                    |                      |
drawMap                | Visualizes coal plants on a US    | None                 |
                       | map with color-coding based on     |                      |
                       | retirement status                  |                      |
---------------------------------------------------------------------------------------
                       |                                    |                      |
drawComponentsMap      | Shows multiple maps of US coal    | None                 |
                       | plants, faceted by component       |                      |
                       | groups                             |                      |
---------------------------------------------------------------------------------------
```
