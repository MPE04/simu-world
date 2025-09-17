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
        num_cities = len(city_data)
        graph = nx.erdos_renyi_graph(n=num_cities, p=1)  # fully connected
        self.grid = Network(graph, capacity=1, random=self.random)

        # --- Création des villes ---
        City.create_agents(
            self,
            num_cities,
            food=0,
            cell=list(self.grid.all_cells),
            name=list(city_data.keys())
        )
        
        print (city_data)

        # --- Création des PNJ (agents et travailleurs) ---
        for city_name, infos in city_data.items():
            workers = infos["workers"]
            agents = infos["agents"]

            PNJ.create_agents(model=self, n=workers, is_producer=True)
            PNJ.create_agents(model=self, n=agents, is_producer=False)

        # --- Collecteur de données ---
        self.datacollector = mesa.datacollection.DataCollector(
            model_reporters={"food_in_city": food_in_city},
            agent_reporters={
                "is_producer": "is_producer",
                "food": lambda a: getattr(a, "food", None)
            },
        )

    def step(self):
        self.agents.shuffle_do("step")
        self.datacollector.collect(self)
