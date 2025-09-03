import mesa

# Data visualization tools.
import seaborn as sns

# Has multi-dimensional arrays and matrices. Has a large collection of
# mathematical functions to operate on these arrays.
import numpy as np

# Data manipulation and analysis.
import pandas as pd

from mesa.visualization import SolaraViz

# -------- Agent --------
class Citizen(mesa.Agent):
    def __init__(self, model, is_producer=False):
        super().__init__(model)
        self.is_producer = is_producer
        self.tick_counter = 00

    def step(self):
        # Tous les agents consomment 1 nourriture
        if self.model.city_food > 0:
            self.model.city_food -= 1

        # Les producteurs produisent tous les 5 ticks
        if self.is_producer:
            self.tick_counter += 1
            if self.tick_counter % 5 == 0:
                self.model.city_food += 30


# -------- Modèle --------
class City(mesa.Model):
    def __init__(self, N=100, workers=20):
        super().__init__()
        self.num_agents = N
        # self.schedule = mesa.time.SimultaneousActivation(self)

        # Stock de nourriture dans la ville
        self.city_food = 0
        
        Citizen.create_agents(model=self, n=workers, is_producer=True)
        Citizen.create_agents(model=self, n=N-workers, is_producer=False)

        # Collecteur de données
        self.datacollector = mesa.datacollection.DataCollector(
            model_reporters={"CityFood": lambda m: m.city_food}
        )

    def step(self):
        self.agents.shuffle_do("step")
        self.datacollector.collect(self)
        


# -------- Visualisation Solara --------
def get_chart(model):
    """Retourne les données du graphe"""
    return model.datacollector.get_model_vars_dataframe()

viz = mesa.visualization.SolaraViz(
    City,
    params={"N": 100, "workers": 20},  # paramètres initiaux du modèle
    model_reporters={"CityFood": lambda m: m.city_food},  # suivi du stock
)

# Lance l'interface si on exécute le script
if __name__ == "__main__":
    viz.run()
