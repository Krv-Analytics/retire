"""
Retire: A data-driven approach to strategizing US coal plant retirement.

This package provides tools and data for analyzing coal plant retirement
strategies based on the research published in "Strategies to Accelerate US 
Coal Power Phaseout Using Contextual Retirement Vulnerabilities" in Nature Energy.

The package includes:
- Coal plant datasets with retirement vulnerabilities and contextual factors
- Network analysis tools for understanding plant relationships
- Visualization utilities for exploring retirement strategies
- Manuscript results and analysis outputs

Example usage:
    >>> from retire import Retire, Explore
    >>> retire_obj = Retire()
    >>> explore = Explore(retire_obj.graph, retire_obj.raw_df)
    >>> fig, ax = explore.drawMap()
"""

from retire.explore import Explore
from retire.retire import Retire

__version__ = "0.1.0"
__all__ = ['Retire', 'Explore']
