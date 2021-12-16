import meta.Meta as Meta
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import LightSource

start = [0.5, 0.5]

max_steps = 400
step = 1
step_divider = 0.5
quality = 0.00001
quality1 = 0.00001
quality2 = 0.00001




def absV(x): 
    return np.sqrt(x[0]**2 + x[1]**2)

def gradientDescent(coords, step, maximum): 
    coordsArr = []
    k = 0
    while True:
        grad = Meta.dfn(coords[0], coords[1])
        if abs(grad[0]) < quality1 and abs(grad[1]) < quality1:
            return coordsArr
        if k >= maximum:
            return coordsArr
        delta = 0
        while True:
            newCoords = [coords[0] - step * grad[0]/absV(grad), coords[1] - step * grad[1]/absV(grad)]
            delta = Meta.fn(newCoords[0], newCoords[1]) - Meta.fn(coords[0], coords[1])
            k+=1
            if delta < 0 or delta < quality * absV(grad)**2:
                break
            else:
                step = step * step_divider
        first = absV([newCoords[0]- coords[0], newCoords[1] - coords[1]])
        second = abs(delta)
        if first < quality2 and second < quality2:
            return coordsArr
        else:
            coords = newCoords
            k += 1
        coordsArr.append(coords)



coordsArr = gradientDescent(start, step, max_steps)
# x and y axis

  
X, Y = np.meshgrid(Meta.x, Meta.y)
Z = Meta.fn(X, Y)
 
fig = plt.figure()
ax = plt.axes(projection ='3d')
ls = LightSource(270, 45)
rgb = ls.shade(Z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors=rgb,
                        alpha=0.15,
                       linewidth=0, antialiased=False, shade=False)

for i in range(len(coordsArr) - 1):
    [x, y] = coordsArr[i]
    [xN, yN] = coordsArr[i+1]
    ax.plot3D([x, xN], [y, yN], [Meta.fn(x, y), Meta.fn(xN, yN)], 'red')
print(coordsArr)
plt.show()




