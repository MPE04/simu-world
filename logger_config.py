# logger_config.py
import logging
import sys
from pathlib import Path

LOG_FILE = Path(__file__).parent / "simulation.log"

def get_logger(name: str) -> logging.Logger:
    """
    Retourne un logger global configuré avec :
      - Fichier : tous les niveaux (DEBUG+), réinitialisé à chaque lancement
      - Console : seulement les erreurs et critiques
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.hasHandlers():
        logger.propagate = False  # Empêche les doublons

        # --- Handler console (uniquement erreurs) ---
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.ERROR)

        # --- Handler fichier (tout) ---
        # mode="w" => écrase le fichier à chaque démarrage
        file_handler = logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)

        # --- Format commun ---
        formatter = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # --- Ajout des handlers ---
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
