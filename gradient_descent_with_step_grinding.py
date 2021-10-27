import meta
import numpy as np

start = [0.53, .35]

max_points = 50
step = 1
step_minimizer = 0.5
quality = 0.000001

def grad_abs(x): 
    return np.sqrt(x[0]**2 + x[1]**2)

def gradientDescent(): 
    while(True):
        gr = meta.dfn(start[0], start[1])
        if gr[0] == 0 and gr[0] == 0:
            break
        h = gr/ grad_abs(gr)
        new_start = start - step * h
        if meta.fn(start[0], start[1]) > meta.fn(new_start[0], new_start[1]):
            start = new_start
        else:
            step = step_minimizer * step
        print(start)

gradientDescent()



