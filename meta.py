import numpy as np

# first
# def fn(x, y):
#     return x**4 + y**4 + np.sqrt(2 + x**2 + y**2) - 2*x - 3*y
# def dfn(x, y):
#     return [4*x**3 + x/np.sqrt(x**2 + y**2 + 2) - 2, 4*y**3 + y/np.sqrt(x**2 + y**2 + 2) + 3]
# x = np.linspace(-3, 3, 100)
# y = np.linspace(-3, 3, 100)
# radius = 10
# second
def fn(x, y):
    return x**2 + y**2 - np.cos(18*x) - np.cos(18*y)
def dfn(x, y):
    return [x*2 + 18*np.sin(18*x), y*2 + 18*np.sin(18*y)]

x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
radius = 1