from mesa.discrete_space import FixedAgent

# Has multi-dimensional arrays and matrices. Has a large collection of
# mathematical functions to operate on these arrays.
import numpy as np

# Data manipulation and analysis.
import pandas as pd

# -------- Agent --------
class City(FixedAgent):
    def __init__(self, model, food, cell):
        super().__init__(model)
        self.food = food
        self.cell = cell
        self.type = "City"

    def step(self):
        pass
        
