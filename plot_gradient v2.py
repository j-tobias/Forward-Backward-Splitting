import numpy as np
import matplotlib.pyplot as plt
from gradient import *

# Your existing gradient and function functions...

# Create a sample space using meshgrid
x1_vals = np.linspace(-10, 10, 50)
x2_vals = np.linspace(-10, 10, 50)
X1, X2 = np.meshgrid(x1_vals, x2_vals)

# Evaluate the function on the samples
M = np.array([[1, 2]])  # Adjust the values accordingly
y = np.array([3])       # Adjust the value accordingly
tau = 0.1               # Adjust the value accordingly
function_values = np.zeros((50, 50))

for i in range(50):
    for j in range(50):
        function_values[i, j] = function([X1[i, j], X2[i, j]], M, y, tau)

# Compute gradients on the samples
gradients = np.zeros((50, 50, 2))

for i in range(50):
    for j in range(50):
        gradients[i, j] = gradient([X1[i, j], X2[i, j]], M, y, tau)

# Create the 2D plot with arrows representing gradients
fig, ax = plt.subplots()
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_title('Function Surface with Gradients')

# Plot the function surface
surf = ax.contourf(X1, X2, function_values, levels=20, cmap='viridis')

# Add arrows representing gradients
arrow_scale = 0.9  # Adjust the arrow length
for i in range(0, 50, 5):
    for j in range(0, 50, 5):
        x, y = X1[i, j], X2[i, j]
        grad_x, grad_y = gradients[i, j]
        ax.arrow(x, y, grad_x * arrow_scale, grad_y * arrow_scale, head_width=0.25, head_length=0.25, fc='red', ec='red')

# Add colorbar
cbar = plt.colorbar(surf, ax=ax)
cbar.ax.set_ylabel('Function Value')

plt.show()
