"""
Visualization and exploration tools for coal plant network analysis.

This module provides comprehensive visualization capabilities for analyzing
coal plant networks and retirement strategies. The main Explore class offers
methods for creating network graphs, geographic maps, heatmaps, and interactive
visualizations to understand plant relationships and retirement patterns.

Classes
-------
Explore : Main visualization class for network and geographic analysis

Key Visualization Methods
------------------------
- drawGraph : Network graph visualization with customizable node coloring
- drawMap : Interactive geographic map of coal plants
- drawHeatMap : Heatmap visualization of grouped plant characteristics  
- drawDotPlot : Dot plot showing feature distributions across groups
- drawSankey : Sankey flow diagram of retirement proximity transitions
- drawBar : Stacked bar chart of plant counts by proximity group

Examples
--------
>>> from retire import Retire
>>> from retire.explore import Explore
>>> retire_obj = Retire()
>>> explore = Explore(retire_obj.graph, retire_obj.raw_df)
>>> 
>>> # Create network visualization
>>> fig, ax = explore.drawGraph(col='ret_STATUS')
>>> 
>>> # Create interactive map
>>> fig, _ = explore.drawMap()
"""

from .explore import Explore

__all__ = ['Explore']
