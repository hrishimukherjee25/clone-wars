import matplotlib.pyplot as plt

# Data for the current spread times and their Gott Time Principle ranges
actions = ['Mimic', 'Mock', 'Clone']
current_spread_times = [40, 20, 80]
lower_bounds = [40/39, 20/39, 80/39]
upper_bounds = [40*39, 20*39, 80*39]

# Plotting the spread times with Gott Time Principle ranges
fig, ax = plt.subplots(figsize=(10, 6))

# Current spread times
ax.bar(actions, current_spread_times, color=['blue', 'orange', 'green'], label='Current Spread Time')

# Error bars for the Gott Time Principle ranges
ax.errorbar(actions, current_spread_times, yerr=[current_spread_times, upper_bounds], fmt='o', color='red', label='Gott Time Principle Range')

ax.set_title('Spread Times with Gott Time Principle Ranges')
ax.set_ylabel('Spread Time (days)')
ax.set_xlabel('Actions')
ax.legend()

plt.show()
