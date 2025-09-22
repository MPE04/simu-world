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

# --- Créer le modèle ---
model = World(city_data)

# --- Créer les composants dynamiquement ---
plot_components = []
i=1
for city_name in city_data.keys():
    # 🔑 chaque ville aura sa propre clé dans le DataCollector : "food_<ville>"
    comp, _ = make_plot_component(f"food_{city_name}")
    plot_components.append((comp, i))  # tout sur la page 1
    i=i+1

# --- Créer le renderer ---
renderer = SpaceRenderer(model, backend="altair")
renderer.draw_structure(
    node_kwargs={"color": "black", "filled": False, "strokeWidth": 5},
    edge_kwargs={"strokeDash": [6, 1]},
)
renderer.draw_agents(agent_portrayal)

# --- Déclarer les composants avec leur page ---
components = plot_components

# --- Créer l'interface Solara ---
page = SolaraViz(
    model,
    renderer,                # sera sur la page 0
    components=components,   # autres composants sur leurs pages
    model_params={"city_data": {"value": city_data}},
    name="Test MPE",
)
