Explore Module
==============

The ``explore`` module provides comprehensive visualization tools for coal plant network analysis.

.. automodule:: retire.explore.explore
   :members:
   :undoc-members:
   :show-inheritance:

Main Classes
------------

.. autoclass:: retire.explore.explore.Explore
   :members:
   :special-members: __init__
   :exclude-members: __weakref__

Utility Functions
----------------

.. automodule:: retire.explore.utils
   :members:
   :undoc-members:
   :show-inheritance:

Visualization Methods
---------------------

Network Visualizations
~~~~~~~~~~~~~~~~~~~~~~

Methods for visualizing the THEMA graph structure and component relationships:

.. automethod:: retire.explore.explore.Explore.drawGraph
   :noindex:

.. automethod:: retire.explore.explore.Explore.drawComponent
   :noindex:

.. automethod:: retire.explore.explore.Explore.drawPathDistance
   :noindex:

Statistical Visualizations
~~~~~~~~~~~~~~~~~~~~~~~~~~

Methods for creating statistical visualizations of coal plant data:

.. automethod:: retire.explore.explore.Explore.drawHeatMap
   :noindex:

.. automethod:: retire.explore.explore.Explore.drawDotPlot
   :noindex:

Flow and Distribution Charts
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Methods for visualizing distributions and flows between categories:

.. automethod:: retire.explore.explore.Explore.drawBar
   :noindex:

.. automethod:: retire.explore.explore.Explore.drawSankey
   :noindex:

Geographic Visualizations
~~~~~~~~~~~~~~~~~~~~~~~~~

Methods for visualizing coal plants on geographic maps:

.. automethod:: retire.explore.explore.Explore.drawMap
   :noindex:

.. automethod:: retire.explore.explore.Explore.drawComponentsMap
   :noindex:

Analysis Methods
----------------

Graph Analysis
~~~~~~~~~~~~~

Methods for analyzing the network structure and identifying patterns:

.. automethod:: retire.explore.explore.Explore.get_target_nodes
   :noindex:

.. automethod:: retire.explore.explore.Explore.get_shortest_distances_to_targets
   :noindex:

Data Processing
~~~~~~~~~~~~~~

Methods for processing and enriching the underlying datasets:

.. automethod:: retire.explore.explore.Explore.generate_THEMAGrah_labels
   :noindex:

.. automethod:: retire.explore.explore.Explore.assign_group_ids_to_rawdf
   :noindex:

.. automethod:: retire.explore.explore.Explore.assign_group_ids_to_cleandf
   :noindex:
