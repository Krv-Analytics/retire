# retire/retire.py


import pandas as pd
from importlib.resources import files
from retire.data import load_dataset, load_graph


class Retire:
    """
    Main analysis class for coal plant retirement strategies.
    
    The Retire class provides access to coal plant data and manuscript results
    from "Strategies to Accelerate US Coal Power Phaseout Using Contextual 
    Retirement Vulnerabilities" published in Nature Energy. It loads the primary
    dataset and associated network graph for analysis.
    
    Attributes
    ----------
    raw_df : pandas.DataFrame
        The complete US coal plants dataset containing plant characteristics,
        retirement status, and contextual vulnerabilities.
    graph : networkx.Graph
        Network graph representing relationships between coal plants based on
        similarity metrics and contextual factors.
    
    Examples
    --------
    >>> retire = Retire()
    >>> group_analysis = retire.get_group_report()
    >>> explanations = retire.get_target_explanations()
    """

    def __init__(self):
        """
        Initialize the Retire analysis object.
        
        Loads the US coal plants dataset and associated network graph from
        the package resources. The dataset contains information on plant
        characteristics, retirement vulnerabilities, and contextual factors.
        """
        self.raw_df = load_dataset()    
        self.graph = load_graph() 

    def get_plant_level_analysis(self, ORISPL: str):
        """
        Get detailed analysis for a specific coal plant.
        
        Parameters
        ----------
        ORISPL : str
            The ORIS plant code (Office of Regulatory Information Systems)
            identifying the specific coal plant to analyze.
            
        Returns
        -------
        dict or pandas.DataFrame
            Plant-specific analysis results including retirement vulnerabilities,
            contextual factors, and strategic recommendations.
            
        Notes
        -----
        This method is currently not implemented and will be added in future versions.
        """
        pass 

    def get_group_report(self):
        """
        Load the group-level analysis results from the manuscript.
        
        Returns
        -------
        pandas.DataFrame
            Group analysis results containing aggregated statistics and
            characteristics for each identified cluster of coal plants
            with similar retirement vulnerabilities.
            
        Examples
        --------
        >>> retire = Retire()
        >>> groups = retire.get_group_report()
        >>> print(groups.columns)
        """
        path = files("retire").joinpath("resources/results/group_analysis.csv")
        return pd.read_csv(path)

    def get_target_explanations(self):
        """
        Load plant-level explanations for retirement targeting strategies.
        
        Returns
        -------
        pandas.DataFrame
            Plant-level explanations containing detailed reasoning for why
            specific plants were identified as priority targets for retirement
            based on contextual vulnerabilities and strategic factors.
            
        Examples
        --------
        >>> retire = Retire()
        >>> explanations = retire.get_target_explanations()
        >>> target_plants = explanations[explanations['priority'] == 'high']
        """
        path = files("retire").joinpath("resources/results/plant_level_match_explanations.csv")
        return pd.read_csv(path)




    
