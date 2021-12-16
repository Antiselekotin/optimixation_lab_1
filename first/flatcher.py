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

def flatcher(coords, step, max): 
    d0 = -Meta.dfn(coords[0], coords[1])
    coordsArr = []
    k = 0