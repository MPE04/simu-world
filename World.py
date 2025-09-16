import mesa


# Has multi-dimensional arrays and matrices. Has a large collection of
# mathematical functions to operate on these arrays.
import numpy as np

# Data manipulation and analysis.
import pandas as pd

from PNJ import PNJ
from City import City   
import networkx as nx
from mesa.discrete_space import CellCollection, Network

def food_in_city(model):
    return [agent.food for agent in model.agents if agent.type == "City"][0]

# -------- Modèle --------
class World(mesa.Model):
    def __init__(self, N, workers):
        super().__init__()
        self.num_agents = N
        # prob = avg_node_degree / num_nodes
        graph = nx.erdos_renyi_graph(n=2, p=1)
        self.grid = Network(graph, capacity=1, random=self.random)
        # self.schedule = mesa.time.SimultaneousActivation(self)

        # Stock de nourriture dans la ville
        self.city_food = 0
        
        City.create_agents(
            self, 
            2, 
            food=self.city_food, 
            cell=list(self.grid.all_cells),
            name=["CityA", "CityB"])
        
        PNJ.create_agents(model=self, n=workers, is_producer=True)
        PNJ.create_agents(model=self, n=N-workers, is_producer=False)

        # Collecteur de données
        self.datacollector = mesa.datacollection.DataCollector(
            model_reporters={"food_in_city": food_in_city},
            agent_reporters={"is_producer": "is_producer", "food": lambda a: getattr(a, "food", None)},
        )

    

    def step(self):
        self.agents.shuffle_do("step")
        self.datacollector.collect(self)
        
