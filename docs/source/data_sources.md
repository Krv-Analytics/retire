# Data Sources

-----------------------------------------------------------------------------------
Dataset              Description                                 Access Function
-----------------------------------------------------------------------------------|
                 |                                            |                    |
Raw Coal Data    | Original US coal plants dataset with       | load_dataset()     |
                 | plant-level and generator-level            |                    |
                 | information                                |                    |
------------------------------------------------------------------------------------
                 |                                            |                    |
Cleaned Dataset  | Scaled, encoded, and imputed version       | load_clean_dataset()|
                 | of the dataset suitable for machine        |                    |
                 | learning and statistical analysis          |                    |
-------------------------------------------------------------------------------------
                 |                                            |                    |
UMAP Projection  | Low-dimensional embedding of the           | load_projection()  |
                 | cleaned data generated using UMAP          |                    |
                 | for visualization and clustering           |                    |
---------------------------------------------------------------------------------------
                 |                                            |                    |
THEMA Graph      | A multiresolution, discrete graph object   | load_graph()       |
                 | constructed from the data for              |                    |
                 | community detection and network analysis   |                    |
---------------------------------------------------------------------------------------
                 |                                            |                    |
Generator Level  | More detailed dataset with                 | load_generator_    |
Dataset          | generator-specific information for         | level_dataset()    |
                 | coal plants                                |                    |
---------------------------------------------------------------------------------------
```
