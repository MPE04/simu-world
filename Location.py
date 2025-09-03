import mesa


# Has multi-dimensional arrays and matrices. Has a large collection of
# mathematical functions to operate on these arrays.
import numpy as np

# Data manipulation and analysis.
import pandas as pd

from PNJ import PNJ


# -------- Modèle --------
class Location(mesa.Model):
    def __init__(self, N, workers):
        super().__init__()
        self.num_agents = N
        # self.schedule = mesa.time.SimultaneousActivation(self)

        # Stock de nourriture dans la ville
        self.city_food = 0
        
        PNJ.create_agents(model=self, n=workers, is_producer=True)
        PNJ.create_agents(model=self, n=N-workers, is_producer=False)

        # Collecteur de données
        self.datacollector = mesa.datacollection.DataCollector(
            model_reporters={"CityFood": lambda m: m.city_food}
        )

    def step(self):
        self.agents.shuffle_do("step")
        self.datacollector.collect(self)
        
