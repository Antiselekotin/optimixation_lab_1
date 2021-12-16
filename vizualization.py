from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import LightSource
import meta.Meta as Meta
 
 

 
# x and y axis

  
X, Y = np.meshgrid(Meta.x, Meta.y)
Z = Meta.fn(X, Y)
 
fig = plt.figure()
ax = plt.axes(projection ='3d')
ls = LightSource(270, 45)
rgb = ls.shade(Z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors=rgb,
                       linewidth=0, antialiased=False, shade=False)
plt.show()