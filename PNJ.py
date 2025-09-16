import mesa

# Has multi-dimensional arrays and matrices. Has a large collection of
# mathematical functions to operate on these arrays.
import numpy as np

# Data manipulation and analysis.
import pandas as pd

# -------- Agent --------
class PNJ(mesa.Agent):
    def __init__(self, model, is_producer=False):
        super().__init__(model)
        self.is_producer = is_producer
        self.tick_counter = 0
        self.type = "PNJ"

    def step(self):
        # Tous les agents consomment 1 nourriture
        if self.model.agents[0].food > 0:
            self.model.agents[0].food -= 1

        # Les producteurs produisent tous les 5 ticks
        if self.is_producer:
            self.tick_counter += 1
            if self.tick_counter % 5 == 0:
                self.model.agents[0].food += 30
        
