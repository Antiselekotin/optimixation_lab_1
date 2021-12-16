import numpy as np
import math


class Meta:
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

        ## excelend
        # return 2* x**2 + x*y + y**2
    def dfn(x, y):
        return [x*2 + 18*np.sin(18*x), y*2 + 18*np.sin(18*y)]

        ## excelend
        # return [4*x + y, x + 2*y]

    def Hfn(x, y):
        return [
            [2 + 324*np.cos(18*x), 0],
            [0, 2 + 324*np.cos(18*y)]
        ]

        ## excelend
        # return [
        #     [4, 1],
        #     [1, 2]
        # ]

    def AntiHfn(x,y):
        return np.matrix(Meta.Hfn(x, y)).getI().getA()

    x = np.linspace(-1000, 1000, 100)
    y = np.linspace(-1000, 1000, 100)


    def gradModule(grad): 
        return math.sqrt(grad[0]*grad[0] + grad[1]*grad[1])

    def isCorrectHesse(hesse):
        return hesse[0][0] > 0 and np.linalg.det(hesse) > 0