import json
from World import World
from mesa.visualization import SolaraViz, make_plot_component, SpaceRenderer
from mesa.visualization.components import AgentPortrayalStyle


def agent_portrayal(agent):
    return AgentPortrayalStyle(
        color="green" if agent.food == 0 else "red",
        size=20
    )

# --- Lire le JSON ---
with open("config.json", "r", encoding="utf-8") as f:
    city_data = json.load(f)

# --- Définir model_params avec le paramètre attendu ---
model_params = {
    "city_data": {
        "value": city_data
    }
}

# --- Créer le modèle ---
model = World(city_data)

# --- Créer les composants ---
# ATTENTION : make_plot_component renvoie (component, dependencies)
CityFoodPlot, _ = make_plot_component("food_in_city")

renderer = SpaceRenderer(model, backend="altair")
renderer.draw_structure(
    node_kwargs={"color": "black", "filled": False, "strokeWidth": 5},
    edge_kwargs={"strokeDash": [6, 1]},
)
renderer.draw_agents(agent_portrayal)

# --- Déclarer les composants avec leur page ---
components = [
    (CityFoodPlot, 1),  # CityFoodPlot est maintenant un callable pur
]

# --- Créer l'interface Solara ---
page = SolaraViz(
    model,
    renderer,                # sera sur la page 0
    components=components,   # autres composants sur leurs pages
    model_params=model_params,
    name="Test MPE",
)
