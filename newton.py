from meta.Meta import Meta
from paint.Painter import Painter
import math
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import LightSource

point = [1000, 1000]
# point = [.5, .5]
# point = [1.5, 1.5]
# point = [1, 1]

points = [point]

M = 400
k = 0
quality = 0.00001
quality1 = 0.00001
quality2 = 0.00001


step = None
grad = None
hesse = None

while k < M:
    k += 1
    grad = Meta.dfn(point[0], point[1])
    if Meta.gradModule(grad) < quality:
        break
    hesse = Meta.AntiHfn(point[0], point[1])
    if Meta.isCorrectHesse(hesse):
        step = np.matmul(hesse, grad)
        stepMul = 1
    else:
        step = grad
        stepMul = 1
        newPoint = [point[0] - stepMul*step[0], point[1]- stepMul*step[1]]
        while Meta.fn(newPoint[0], newPoint[1]) > Meta.fn(point[0], point[1]) :
            stepMul = stepMul / 2
            newPoint = [point[0] - stepMul*step[0], point[1]- stepMul*step[1]]
        

    newPoint = [point[0] - stepMul*step[0], point[1]- stepMul*step[1]]

    if math.sqrt((newPoint[1] - point[1])**2 + (newPoint[0] - point[0])**2) < quality1 and abs(Meta.fn(newPoint[0], newPoint[1]) - Meta.fn(point[0], point[1])) < quality2:
        break

    point = newPoint
    points.append(point)
    

print(Meta.fn(point[0], point[1]))

painter = Painter(Meta.x, Meta.y, Meta.fn)
print(points)
painter.paintLinesByPoints(points)