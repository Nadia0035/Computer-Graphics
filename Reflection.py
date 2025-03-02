import matplotlib.pyplot as plt
## Reflection among x axis point is (4,5)
x,y = 4,5
x1,y1= x, -y

plt.scatter(x,y,color='b')
plt.scatter(x1,y1,color='r')

# Show only the x and y axis lines
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

plt.show()