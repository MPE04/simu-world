import mesa
import numpy as np
import pandas as pd
import networkx as nx
from mesa.discrete_space import CellCollection, Network

from PNJ import PNJ
from City import City   

from logger_config import get_logger
logger = get_logger("World")

logger.info("Démarrage du modèle World")


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
        
        if isinstance(city_data, dict) and "value" in city_data:
            city_data = city_data["value"]

        num_cities = len(city_data.keys())
        graph = nx.erdos_renyi_graph(n=num_cities, p=1)
        self.grid = Network(graph, random=self.random)

        self.city_agents = {}  # stocker les agents City par nom

        # --- Création des villes ---
        for city_name, infos in city_data.items():
            workers = infos.get("workers", 1)
            agents = infos.get("workers", 1)
            cell = self.grid.select_random_empty_cell()
            
            city_kwargs = {
                "n": 1,
                "food": 0,
                "cell": self.grid.select_random_empty_cell(),
                "name": city_name,
            }
            if "population" in infos:
                city_kwargs["population"] = infos["population"]

            before = set(self.agents)
            City.create_agents(self, **city_kwargs)
            after = set(self.agents)
            new_city_agents = list(after - before)
            if len(new_city_agents) != 1:
                raise RuntimeError(f"Erreur : attendu 1 agent City, trouvé {len(new_city_agents)}")
            city_agent = new_city_agents[0]

            self.city_agents[city_name] = city_agent  # stocker la référence

            PNJ.create_agents(model=self, 
                              n=workers, 
                              cell=cell, 
                              location=city_agent, 
                              is_producer=True)
            PNJ.create_agents(model=self, 
                              n=agents, 
                              cell=cell, 
                              location=city_agent, 
                              is_producer=False)

        # --- Collecteur de données par ville ---
        model_reporters = {}
        for city_name, city_agent in self.city_agents.items():
            model_reporters[f"food_{city_name}"] = (
                lambda m, c=city_agent: c.food  # 👈 capturer city_agent
            )
            model_reporters[f"pop_{city_name}"] = (
                lambda m, c=city_agent: c.population  # 👈 capturer city_agent
            )

        self.datacollector = mesa.datacollection.DataCollector(
            model_reporters=model_reporters
        )

    def step(self):
        self.agents.shuffle_do("step")
        self.datacollector.collect(self)
