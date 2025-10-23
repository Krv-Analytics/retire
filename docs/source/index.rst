Retire: Coal Plant Retirement Analysis
======================================

Welcome to the documentation for the ``retire`` package, a comprehensive tool for analyzing coal plant retirement strategies based on research published in *Nature Energy*.

.. image:: https://img.shields.io/github/contributors/Krv-Analytics/retire?style=flat-square
   :target: https://github.com/Krv-Analytics/retire/graphs/contributors
   :alt: Contributors

.. image:: https://img.shields.io/badge/License-BSD%203--Clause-blue?style=flat-square
   :target: LICENSE.md
   :alt: License: BSD 3-Clause

.. image:: https://img.shields.io/badge/python-3.10%2B-blue?style=flat-square&logo=python
   :target: https://www.python.org/
   :alt: Python 3.10+

.. image:: https://img.shields.io/pypi/v/retire-coal?style=flat-square
   :target: https://pypi.org/project/retire-coal/
   :alt: PyPI version

.. image:: https://img.shields.io/badge/docs-available-green?style=flat-square
   :target: docs/
   :alt: Documentation

.. image:: https://img.shields.io/badge/web-krv.ai-black?style=flat-square&logo=vercel
   :target: https://krv.ai
   :alt: Website

.. image:: https://img.shields.io/badge/LinkedIn-Krv%20Analytics-blue?style=flat-square&logo=linkedin
   :target: https://www.linkedin.com/company/krv-analytics
   :alt: LinkedIn

.. image:: https://img.shields.io/badge/Email-team@krv.ai-fe2b27?style=flat-square&logo=gmail
   :target: mailto:team@krv.ai
   :alt: Email

.. image:: https://img.shields.io/badge/Nature%20Energy-Manuscript-darkgreen?style=flat-square&logo=bookstack
   :target: https://www.nature.com/articles/s41560-025-01871-0
   :alt: Nature Energy Manuscript

.. image:: https://img.shields.io/badge/Nature%20Energy-Research%20Briefing-darkgreen?style=flat-square&logo=bookstack
   :target: https://www.nature.com/articles/s41560-025-01872-z
   :alt: Nature Energy Research Briefing

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

.. plot::
   :context: close-figs
   :include-source: True

   from retire import Retire, Explore
   
   # Load data and create analysis objects
   retire_obj = Retire()
   explore = Explore(retire_obj.graph, retire_obj.raw_df)

   # Visualize the network
   fig, ax = explore.drawGraph(col="ret_STATUS")


.. raw:: html

   <p style="font-size:0.8em;">Figure adapted from Gathrid et al. (2025, <em>Nature Energy</em>).</p>


.. ipython:: python

   from retire import Retire, Explore
   
   retire_obj = Retire()
   
   retire_obj.get_group_report().head()
   retire_obj.get_target_explanations().head()



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

.. toctree::
   :maxdepth: 1
   :caption: Tutorials:

   tutorials


