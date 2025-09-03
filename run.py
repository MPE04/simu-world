from money_model import MoneyModel

from dynamic_world import City

# Data visualization tools.
import seaborn as sns
import matplotlib.pyplot as plt

all_wealth = []
model = City(100, 20)    
for _ in range(30):
    model.step()

# Store the results
# for agent in model.agents:
#     all_wealth.append(agent.wealth)

# Use seaborn
# g = sns.histplot(all_wealth, discrete=True)
# g.set(title="Wealth distribution", xlabel="Wealth", ylabel="number of agents")

food = model.datacollector.get_model_vars_dataframe()
# Plot the Gini coefficient over time
g = sns.lineplot(data=food)
g.set(title="Step", ylabel="Food over time");

plt.show()