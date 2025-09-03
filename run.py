from dynamic_world import City

# Data visualization tools.
import seaborn as sns
import matplotlib.pyplot as plt

model = City(100, 20)    
for _ in range(30):
    model.step()

food = model.datacollector.get_model_vars_dataframe()
# Plot the food over time
g = sns.lineplot(data=food)
g.set(title="Step", ylabel="Food over time")

plt.show()