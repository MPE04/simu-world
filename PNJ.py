import mesa
from logger_config import get_logger

logger = get_logger("PNJ")

class PNJ(mesa.Agent):
    def __init__(self, model, cell, location, is_producer=False):
        super().__init__(model)
        self.is_producer = is_producer
        self.tick_counter = 0
        self.cell = cell
        self.location = location

        logger.debug(f"Création d'un PNJ (is_producer={self.is_producer}) "
                     f"à {getattr(self.location, 'name', 'Inconnu')}")

    def step(self):
        if self.location.food > 0:
            self.location.food -= 1
            logger.debug(f"{self.unique_id} consomme 1 nourriture, reste {self.location.food}")

        if self.is_producer:
            self.tick_counter += 1
            if self.tick_counter % 5 == 0:
                self.location.food += 30
                logger.info(f"{self.unique_id} PRODUIT 30 nourriture -> total {self.location.food}")
