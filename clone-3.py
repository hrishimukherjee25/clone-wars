import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data preparation
actions = ['Mimic', 'Mock', 'Clone']
spread_times_without_gott = [40, 20, 80]
lower_bounds_gott = [40/39, 20/39, 80/39]
upper_bounds_gott = [40*39, 20*39, 80*39]
colors = ['blue', 'orange', 'green']

# Function to create a sphere
def create_sphere(radius, center):
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = radius * np.outer(np.cos(u), np.sin(v)) + center[0]
    y = radius * np.outer(np.sin(u), np.sin(v)) + center[1]
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v)) + center[2]
    return x, y, z

# Function to perturb the surface of the sphere
def perturb_surface(x, y, z, factor=0.1):
    noise_x = np.random.normal(0, factor, x.shape)
    noise_y = np.random.normal(0, factor, y.shape)
    noise_z = np.random.normal(0, factor, z.shape)
    return x + noise_x, y + noise_y, z + noise_z

# Plotting the data in 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Creating and plotting the inflated hyperspheres with perturbation
radius = 5  # Increased radius for inflation
for i in range(len(actions)):
    x, y, z = create_sphere(radius, (spread_times_without_gott[i], lower_bounds_gott[i], upper_bounds_gott[i]))
    x, y, z = perturb_surface(x, y, z, factor=0.5)  # Increased perturbation factor
    ax.plot_surface(x, y, z, color=colors[i], alpha=0.6)

# Adding labels
for i, action in enumerate(actions):
    ax.text(spread_times_without_gott[i], lower_bounds_gott[i], upper_bounds_gott[i], action)

ax.set_title('3D Translation with Inflated Hyperspheres and Perturbed Surface')
ax.set_xlabel('Spread Time (without Gott)')
ax.set_ylabel('Lower Bound (Gott)')
ax.set_zlabel('Upper Bound (Gott)')

plt.show()
