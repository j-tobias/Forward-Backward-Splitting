import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from gradient import *

# Your existing gradient and function functions...

# Create a sample space using meshgrid
x1_vals = np.linspace(-10, 10, 50)
x2_vals = np.linspace(-10, 10, 50)
X1, X2 = np.meshgrid(x1_vals, x2_vals)
samples = np.stack([X1, X2], axis=-1)

# Evaluate the function on the samples
M = np.array([[1, 2]])  # Adjust the values accordingly
y = np.array([3])       # Adjust the value accordingly
tau = 0.1               # Adjust the value accordingly
function_values = np.zeros((50, 50))

for i in range(50):
    for j in range(50):
        function_values[i, j] = Objective(M, samples[i, j], y, tau)

# Compute gradients on the samples
gradients = np.zeros((50, 50, 2))

for i in range(50):
    for j in range(50):
        gradients[i, j] = GradObjective(M, samples[i, j], y, tau)

# Plot both results in one plot
fig = plt.figure(figsize=(10, 5))

# 3D plot of the function values
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X1, X2, function_values, cmap='viridis')
ax1.set_xlabel('X1')
ax1.set_ylabel('X2')
ax1.set_zlabel('Function Value')
ax1.set_title('Function Values')

# 2D plot of the gradients as arrows
ax2 = fig.add_subplot(122)
ax2.quiver(X1, X2, gradients[:, :, 0], gradients[:, :, 1], angles='xy')
ax2.set_xlabel('X1')
ax2.set_ylabel('X2')
ax2.set_aspect('equal')
ax2.set_title('Gradients')

plt.tight_layout()
plt.show()
