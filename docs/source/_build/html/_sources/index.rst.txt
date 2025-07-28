Retire: Coal Plant Retirement Analysis
======================================

Welcome to the documentation for the ``retire`` package, a comprehensive tool for analyzing coal plant retirement strategies based on research published in *Nature Energy*.

.. image:: https://img.shields.io/badge/python-3.12+-blue.svg
   :target: https://www.python.org/downloads/
   :alt: Python Version

.. image:: https://img.shields.io/badge/License-MIT-green.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License

Overview
--------

The ``retire`` package provides data and analysis tools for US coal plant retirement analysis based on research published in *Nature Energy*.

**Key Features:**

- **Comprehensive Dataset**: Detailed coal plant data with operational and contextual factors
- **Network Analysis**: Analyze plant relationships using similarity metrics  
- **Visualization Suite**: Rich plotting capabilities for retirement patterns
- **Research Reproducibility**: Access to manuscript results and analysis

Quick Start
-----------

.. code-block:: python

   from retire import Retire, Explore
   
   # Load data and create analysis objects
   retire_obj = Retire()
   explore = Explore(retire_obj.graph, retire_obj.raw_df)
   
   # Visualize the network
   fig, ax = explore.drawGraph(col='ret_STATUS')
   
   # Create geographic map
   fig, ax = explore.drawMap()
   
   # Get manuscript results
   group_analysis = retire_obj.get_group_report()
   explanations = retire_obj.get_target_explanations()

.. toctree::
   :maxdepth: 2
   :caption: Getting Started:

   usage_guide
   data_sources
   visualization_methods
   configuration

.. toctree::
   :maxdepth: 2
   :caption: API Reference:

   retire
   data
   explore

.. toctree::
   :maxdepth: 1
   :caption: Development:

   development/testing


