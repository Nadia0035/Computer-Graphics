import matplotlib.pyplot as plt
# from (10,11) to (16,21)
x1,y1= 10,11
x2,y2 = 16,21
dx = x2-x1
dy= y2-y1
m= dy/dx
print(m)
points=[]
points.append((x1,y1))
xi,yi= x1,y1
while xi!=x2 and yi!=y2:
    if(abs(dx)>=abs(dy)):
        xi= xi+1
        yi= yi + m
    else:
        yi=yi+1
        xi= xi+ 1/m
        
        
    points.append((xi,yi))
    
    
points.append((x2,y2))
print(points)
   

x = [point[0] for point in points]
y = [point[1] for point in points]

plt.plot(x,y,color='b',marker='o')

plt.show()