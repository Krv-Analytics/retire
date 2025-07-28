"""
Example configurations for visualization methods.

This module provides pre-configured dictionaries for creating sophisticated
visualizations using the Explore class methods. These configurations demonstrate
best practices for heatmap and dot plot visualizations of coal plant data.

Available Configurations
------------------------
heatmap_config : dict
    Configuration for creating grouped heatmap visualizations with proper
    categorization, aggregations, and derived columns.
dotplot_config : dict  
    Configuration for creating dot plot visualizations showing feature
    distributions across plant groups with normalized coloring.

Examples
--------
>>> from retire import Retire, Explore
>>> from retire.examples import heatmap_config, dotplot_config
>>> 
>>> retire_obj = Retire()
>>> explore = Explore(retire_obj.graph, retire_obj.raw_df)
>>> 
>>> # Create heatmap using pre-configured settings
>>> fig, ax = explore.drawHeatMap(heatmap_config)
>>> 
>>> # Create dot plot with configuration
>>> clean_df = load_clean_dataset()  # from retire.data
>>> fig, ax = explore.drawDotPlot(clean_df, dotplot_config)
"""

from retire.examples.heatmap_config import heatmap_config
from retire.examples.dotplot_config import dotplot_config

__all__ = ['heatmap_config', 'dotplot_config']
