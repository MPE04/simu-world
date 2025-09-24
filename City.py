from mesa.discrete_space import FixedAgent

# Has multi-dimensional arrays and matrices. Has a large collection of
# mathematical functions to operate on these arrays.
import numpy as np

# Data manipulation and analysis.
import pandas as pd
from pathlib import Path

from logger_config import get_logger
log_file = Path(__file__).parent / "city.log"
logger = get_logger("City", log_file=str(log_file))



# -------- Agent --------
class City(FixedAgent):
    def __init__(self, model, food, cell, name, population=None, ressources=None):
        super().__init__(model)
        self.food = food
        self.cell = cell
        self.name = name
        self.population = population if population is not None else self.random.randint(0, 10**6)
        logger.info(f"Création de la ville {self.name} avec population initiale {self.population}")
        self.ressources = ressources if ressources is not None else {}
        logger.info(f"Ressources initiales pour {self.name} : {self.ressources}")
        
        self.tick_counter = 0

    def step(self):
        self.tick_counter += 1
        if self.tick_counter % 10 == 0:
            disparition = int(self.population * 0.0002 * self.random.random())
            ajout = int(self.population * 0.0003 * self.random.random())
            self.population = max(0, self.population - disparition + ajout)
            logger.info(f"{self.name} population mise à jour : {self.population}, disparition={disparition}, ajout={ajout}")
    
