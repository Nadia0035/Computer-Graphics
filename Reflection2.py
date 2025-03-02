## Reflection among y axis point is (4,5)
## here is have added label to make the graph look better

import matplotlib.pyplot as plt

x, y = 4, 5
x1, y1 = -x,y

# Create the plot
plt.scatter(x, y, color='b', label='(x, y)')
plt.scatter(x1, y1, color='r', label='(x1, y1)')

# Show only the x and y axis lines
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

# Add labels and legend
plt.legend()
plt.show()