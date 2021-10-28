from sympy import diff, symbols, cos, sqrt

X = [0.5, 0.5]
epsilon_1 = 0.01
epsilon_2 = 0.5
M = 10
k = 0

def f1(x, y):
    return ((x ** 4) + (y ** 4) + sqrt(2 + (x ** 2) + (y ** 2)) - (2 * x) + (3 * y))

def f2(x, y):
    return ((x ** 2) + (y ** 2) - cos(18 * x) - cos(18 * y))

def grad(x1, y1, f):
    x, y = symbols('x y')
    diff1 = (diff(f(x, y), x)).subs({x:x1, y:y1})
    diff2 = (diff(f(x, y), y)).subs({x:x1, y:y1})
    return [diff1, diff2]

print(grad(X[0], X[1], f1))