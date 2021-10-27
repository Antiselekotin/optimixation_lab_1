import numpy as np

# first
# def fn(x, y):
#     return x**4 + y**4 + np.sqrt(2 + x**2 + y**2) - 2*x - 3*y
# x = np.linspace(-10, 10, 100)
# y = np.linspace(-10, 10, 100)
# radius = 10
# second
def fn(x, y):
    return x**2 + y**2 - np.cos(18*x) - np.cos(18*y)
def dfn(x, y):
    return [x*2 + 18*np.sin(18*x), y*2 + 18*np.sin(18*y)]

x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
radius = 1