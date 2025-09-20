import mesa

# Has multi-dimensional arrays and matrices. Has a large collection of
# mathematical functions to operate on these arrays.
import numpy as np

# Data manipulation and analysis.
import pandas as pd

# -------- Agent --------
class PNJ(mesa.Agent):
    def __init__(self, model, cell, location, is_producer=False):
        super().__init__(model)
        self.is_producer = is_producer
        self.tick_counter = 0
        self.type = "PNJ"
        self.cell = cell
        self.location = location

    def step(self):
        # Tous les agents consomment 1 nourriture
        if self.location.food > 0:
            self.location.food -= 1

        # Les producteurs produisent tous les 5 ticks
        if self.is_producer:
            self.tick_counter += 1
            if self.tick_counter % 5 == 0:
                self.location.food += 30
        
