from World import World

from mesa.visualization import SolaraViz, make_plot_component, SpaceRenderer
from mesa.visualization.components import AgentPortrayalStyle

def agent_portrayal(agent):
    if agent.food == 0 :
        return AgentPortrayalStyle(color="green", size=20)
    else:
        return AgentPortrayalStyle(color="red", size=20)

agentNumber = 100
workerNumber = 20
stepNumber = 30

# --- Run simulation and plot ---
model = World(agentNumber, workerNumber)    

# --- SolaraViz dashboard ---
model_params = {
    "N": {
        "type": "SliderInt",
        "value": 50,
        "label": "Number of agents:",
        "min": 10,
        "max": 100,
        "step": 1,
    },
    "workers": {
        "type": "SliderInt",
        "value": 50,
        "label": "Number of workers:",
        "min": 10,
        "max": 100,
        "step": 1,
    },
}

CityFoodPlot = make_plot_component("food_in_city")

renderer = SpaceRenderer(model, backend="altair")

renderer.draw_structure(
    node_kwargs={"color": "black", "filled": False, "strokeWidth": 5},
    edge_kwargs={"strokeDash": [6, 1]},
)  # Do this to draw the underlying network and customize it
renderer.draw_agents(agent_portrayal)

page = SolaraViz(
    model,  
    renderer,
    components=[CityFoodPlot],
    model_params=model_params,
    name="Test MPE",
)