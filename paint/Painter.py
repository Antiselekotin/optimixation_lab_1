from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import LightSource
import meta.Meta as Meta

class Painter:
    def __init__(self, xRange, yRange, func):
        X, Y = np.meshgrid(xRange, yRange)
        Z = func(X, Y)
        self.func = func
        fig = plt.figure()
        self.ax = plt.axes(projection ='3d')
        ls = LightSource(270, 45)
        rgb = ls.shade(Z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
        self.ax.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors=rgb,
                                alpha=0.15,
                            linewidth=0, antialiased=False, shade=False)
        
    def paintLinesByPoints(self, points):
        for i in range(len(points) - 1):
            [x, y] = points[i]
            [xN, yN] = points[i+1]
            self.ax.plot3D([x, xN], [y, yN], [self.func(x, y), self.func(xN, yN)], 'red')
        
        plt.show()
        
