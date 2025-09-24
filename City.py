from mesa.discrete_space import FixedAgent

# Has multi-dimensional arrays and matrices. Has a large collection of
# mathematical functions to operate on these arrays.
import numpy as np

# Data manipulation and analysis.
import pandas as pd

from logger_config import get_logger
logger = get_logger("City")



# -------- Agent --------
class City(FixedAgent):
    def __init__(self, model, food, cell, name, population=0):
        super().__init__(model)
        self.food = food
        self.cell = cell
        self.name = name
        self.population = self.random.randint(0, 10**6)
        self.tick_counter = 0

    def step(self):
        self.tick_counter += 1
        if self.tick_counter % 10 == 0:
            disparition = int(self.population * 0.02 * self.random.random())
            ajout = int(self.population * 0.03 * self.random.random())
            self.population = max(0, self.population - disparition + ajout)
            logger.info(f"{self.name} population mise à jour : {self.population}, disparition={disparition}, ajout={ajout}")
    
