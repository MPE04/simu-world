from World import World

# Data visualization tools.
import seaborn as sns
import matplotlib.pyplot as plt

agentNumber = 100
workerNumber = 20
stepNumber = 30

model = World(agentNumber, workerNumber)    

for _ in range(stepNumber):
    model.step()

food = model.datacollector.get_model_vars_dataframe()
# Plot the food over time
g = sns.lineplot(data=food)
g.set(title="Step", ylabel="Food over time")

plt.show()