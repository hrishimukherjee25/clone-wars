import pandas as pd
from pandas.plotting import parallel_coordinates
import matplotlib.pyplot as plt

# Data preparation
actions = ['Mimic', 'Mock', 'Clone']
spread_times_without_gott = [40, 20, 80]
lower_bounds_gott = [40/39, 20/39, 80/39]
upper_bounds_gott = [40*39, 20*39, 80*39]
decay_factors = [1.1, 1.05, 1.2]
despair_factors = [1.2, 1.1, 1.3]
adjusted_payoffs = [1 / (spread_times_without_gott[i] * decay_factors[i] * despair_factors[i]) for i in range(3)]

data = {
    'Action': actions,
    'Spread Time (without Gott)': spread_times_without_gott,
    'Lower Bound (Gott)': lower_bounds_gott,
    'Upper Bound (Gott)': upper_bounds_gott,
    'Adjusted Payoff': adjusted_payoffs
}

df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(12, 8))
parallel_coordinates(df, class_column='Action', colormap=plt.get_cmap("Set2"))
plt.title('5D Translation of Spread Times and Payoffs')
plt.ylabel('Values')
plt.xlabel('Dimensions')
plt.grid(True)
plt.show()
