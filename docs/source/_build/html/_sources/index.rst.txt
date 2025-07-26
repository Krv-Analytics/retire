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

The ``retire`` package provides data and analysis tools for understanding and strategizing US coal plant retirement based on contextual vulnerabilities. It implements methods from the research paper *"Strategies to Accelerate US Coal Power Phaseout Using Contextual Retirement Vulnerabilities"* published in Nature Energy.

**Key Features:**

- **Comprehensive Dataset**: Access to detailed coal plant data including operational characteristics, retirement status, and contextual factors
- **Network Analysis**: Tools for analyzing relationships between plants based on similarity metrics  
- **Visualization Suite**: Rich plotting capabilities for exploring retirement patterns and strategies
- **Research Reproducibility**: Direct access to manuscript results and analysis outputs

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
   :caption: User Guide:

   usage_guide
   configuration
   data_sources
   visualization_methods

.. toctree::
   :maxdepth: 2
   :caption: API Reference:

   retire
   data
   explore

.. toctree::
   :maxdepth: 2
   :caption: Development:

   development/data
   development/explorer
   development/testing

.. toctree::
   :maxdepth: 1
   :caption: Additional Resources:

   GitHub Repository <https://github.com/your-org/retire>
   Nature Energy Paper <https://doi.org/your-paper-doi>

