import mesa
import numpy as np
import pandas as pd
import networkx as nx
from mesa.discrete_space import CellCollection, Network

from PNJ import PNJ
from City import City   

def food_in_city(model):
    return [agent.food for agent in model.agents if agent.type == "City"][0]

# -------- Modèle --------
class World(mesa.Model):
    def __init__(self, city_data: dict):
        """
        city_data est un dictionnaire chargé depuis un fichier JSON :
        {
            "Paris": {"agents": 12, "travailleurs": 50},
            "Lyon": {"agents": 8, "travailleurs": 30}
        }
        """
        super().__init__()
        
        # --- Normaliser l'entrée en cas de reset depuis SolaraViz ---
        if isinstance(city_data, dict) and "value" in city_data:
            city_data = city_data["value"]

        # --- Construire un graphe avec autant de noeuds que de villes ---
        num_cities = len(city_data.keys())
        graph = nx.erdos_renyi_graph(n=num_cities, p=1)  # fully connected
        self.grid = Network(graph, random=self.random)

        # --- Création des villes ---
        for city_name, infos in city_data.items():
            workers = infos["workers"]
            agents = infos["agents"]
            cell =self.grid.select_random_empty_cell(),
            City.create_agents(
                self,
                n=1,
                food=0,
                cell=cell,
                name=city_name
            )
            
            PNJ.create_agents(model=self, n=workers, cell=cell, is_producer=True)
            PNJ.create_agents(model=self, n=agents, cell=cell, is_producer=False)

        # # --- Création des PNJ (agents et travailleurs) ---
        # for city_name, infos in city_data.items():
        #     workers = infos["workers"]
        #     agents = infos["agents"]

        #     PNJ.create_agents(model=self, n=workers, is_producer=True)
        #     PNJ.create_agents(model=self, n=agents, is_producer=False)

        # --- Collecteur de données ---
        self.datacollector = mesa.datacollection.DataCollector(
            model_reporters={"food_in_city": food_in_city},
            # agent_reporters={
            #     "is_producer": "is_producer",
            #     "food": lambda a: getattr(a, "food", None)
            # },
        )

    def step(self):
        self.agents.shuffle_do("step")
        self.datacollector.collect(self)
