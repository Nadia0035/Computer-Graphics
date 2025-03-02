#  Mirroring Across Both Axes for point (4,5)
import matplotlib.pyplot as plt
x, y = 4, 5
x1, y1 = -x,-y

# Create the plot
plt.scatter(x, y, color='b', label='(first x, first y)')
plt.scatter(x1, y1, color='r', label='(mirrored x, mirrored y)')

# Show only the x and y axis lines
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

# Add labels and legend
plt.legend()
plt.show()