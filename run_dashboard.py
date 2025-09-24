import json
import pandas as pd
import solara  # ✅ pour le tableau interactif
from World import World
from mesa.visualization import SolaraViz, make_plot_component, SpaceRenderer
from mesa.visualization.components import AgentPortrayalStyle


def agent_portrayal(agent):
    return AgentPortrayalStyle(
        color="green" if agent.food == 0 else "red",
        size=20
    )


# --- Composant tableau basé sur les colonnes existantes du DataCollector ---
def population_table_component(model):
    df = model.datacollector.get_model_vars_dataframe()
    if df.empty:
        return solara.Text("Pas encore de données disponibles")

    last_row = df.iloc[-1]  # Dernière ligne = dernier step
    # Filtrer uniquement les colonnes de population
    pop_data = {col: last_row[col] for col in df.columns if col.startswith("pop_")}

    if not pop_data:
        return solara.Text("Aucune donnée de population collectée")

    # Construire un DataFrame propre pour l'affichage
    table_df = pd.DataFrame(
        [(col.replace("pop_", ""), val) for col, val in pop_data.items()],
        columns=["Ville", "Population"]
    )

    return solara.DataFrame(table_df)


# --- Lire le JSON ---
with open("config.json", "r", encoding="utf-8") as f:
    city_data = json.load(f)

# --- Créer le modèle ---
model = World(city_data)

# --- Créer les composants dynamiquement ---
plot_components = []
i = 1
for city_name in city_data.keys():
    # ✅ Tu as déjà "pop_<ville>" et "food_<ville>" dans le DataCollector
    for t in ["food", "pop"]:
        comp, _ = make_plot_component(f"{t}_{city_name}")
        plot_components.append((comp, i))
    i += 1

# --- Ajouter le tableau des populations sur une nouvelle page ---
plot_components.append((population_table_component, 0))

# --- Créer le renderer ---
renderer = SpaceRenderer(model, backend="altair")
renderer.draw_structure(
    node_kwargs={"color": "black", "filled": False, "strokeWidth": 5},
    edge_kwargs={"strokeDash": [6, 1]},
)
renderer.draw_agents(agent_portrayal)

# --- Créer l'interface Solara ---
page = SolaraViz(
    model,
    renderer,                # sera sur la page 0
    components=plot_components,
    model_params={"city_data": {"value": city_data}},
    name="Test MPE",
)
