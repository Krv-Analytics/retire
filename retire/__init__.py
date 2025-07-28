"""
Retire: A data-driven approach to strategizing US coal plant retirement.

This package provides comprehensive tools and datasets for analyzing coal plant 
retirement strategies based on the research published in "Strategies to Accelerate US 
Coal Power Phaseout Using Contextual Retirement Vulnerabilities" in Nature Energy.

The package enables researchers and policymakers to:
- Analyze coal plant characteristics and retirement vulnerabilities
- Explore network relationships between similar plants
- Visualize retirement patterns and strategic opportunities
- Access manuscript results and detailed explanations

Main Components
---------------
Retire : Primary analysis class providing access to datasets and results
Explore : Visualization class for network analysis and geographic mapping
retire.data : Data loading utilities for various datasets
retire.examples : Configuration examples for visualizations

Key Features
------------
- 914 US coal plants with detailed characteristics and retirement status
- Network graph representing plant similarity relationships  
- Interactive visualizations including maps, network graphs, and flow diagrams
- Manuscript results including group analysis and target explanations
- Generator-level data for detailed technical analysis

Quick Start
-----------
>>> from retire import Retire, Explore
>>> 
>>> # Load data and initialize analysis
>>> retire_obj = Retire()
>>> print(f"Loaded {len(retire_obj.raw_df)} coal plants")
>>> 
>>> # Create visualizations
>>> explore = Explore(retire_obj.graph, retire_obj.raw_df)
>>> fig, ax = explore.drawMap()  # Interactive geographic map
>>> fig, ax = explore.drawGraph(col='ret_STATUS')  # Network graph
>>> 
>>> # Access manuscript results
>>> group_analysis = retire_obj.get_group_report()
>>> explanations = retire_obj.get_target_explanations()

For more detailed examples, see the tutorials/ directory and documentation.
"""

from retire.explore import Explore
from retire.retire import Retire

__version__ = "0.1.0"
__all__ = ['Retire', 'Explore']
