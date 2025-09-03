from World import World

from mesa.visualization import SolaraViz, make_plot_component

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

page = SolaraViz(
    model,  
    components=[CityFoodPlot],
    model_params=model_params,
    name="Test MPE",
)