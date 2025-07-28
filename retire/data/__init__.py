"""
Data loading utilities for the retire package.

This module provides functions to load various coal plant datasets and
network graphs used in the analysis. All data is loaded from package
resources and includes both raw and processed datasets.
"""

from .data import load_dataset
from .data import load_clean_dataset
from .data import load_projection
from .data import load_graph
from .data import load_generator_level_dataset

__all__ = [
    'load_dataset',
    'load_clean_dataset', 
    'load_projection',
    'load_graph',
    'load_generator_level_dataset'
]
