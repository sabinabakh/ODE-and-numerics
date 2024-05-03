import numpy as np
import matplotlib.pyplot as plt

"""
Task (c)
"""

fig, (ax1, ax2) = plt.subplots(2)  # Creating 2 subplots
fig.tight_layout(pad=4)

x1 = np.linspace(0, 1, 200)
x2 = np.linspace(-3, 3, 200)

ax1.plot(x1, np.sin(5 * x1), x1, np.cos(5 * x1), linewidth=0.5, color='black')
ax1.set_xticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
ax1.set_yticks([-2, -1, 0, 1, 2])
ax1.set_xticklabels(['0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1'])

ax1.axis([0, 1, -2, 2])  # xmin, xmax, ymin, ymax
ax1.grid(linestyle='dotted', linewidth=0.4)
ax1.set(xlabel='x', ylabel='y')  # Naming x-, y-axis
ax1.set_title("y = sin(5x) and y = cos(5x)")  # Naming the graph

ax2.plot(x2, np.sin(np.exp(x2)), linewidth=0.5, color='black')
ax2.set_xticks([-3, -2, -1, 0, 1, 2, 3])
ax2.set_yticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
ax2.set_yticklabels(['-1.5', '-1', '-0.5', '0', '0.5', '1', '1.5'])

ax2.axis([-3, 3, -1.5, 1.5])  # xmin, xmax, ymin, ymax
ax2.set(xlabel='x', ylabel='y')  # Naming x-, y-axis
ax2.set_title("y = sin(exp(x))")  # Naming the graph

plt.show()