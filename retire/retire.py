# retire/retire.py


import pandas as pd
from importlib.resources import files
from retire.data import load_dataset, load_graph


class Retire:

    def __init__(self):
        self.raw_df = load_dataset()    
        self.graph = load_graph() 



    def get_plant_level_analysis(self, ORISPL: str): 
        pass 


    def get_group_report(self ): 
        path = files("retire").joinpath("resources/results/group_analysis.csv")
        return pd.read_csv(path)

    def get_target_explanations(self): 
        path = files("retire").joinpath("resources/results/plant_level_match_explanations.csv")
        return pd.read_csv(path)




    
