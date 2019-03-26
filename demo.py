import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3-3*x+1

x = np.linspace(-3,3,100)
plt.axhline(0, c='red')
plt.plot(x, f(x))
plt.show()

from scipy.optimize import brentq, newton
print(brentq(f, -3, 0), brentq(f, 0, 1), brentq(f, 1,3))
print(newton(f, -3), newton(f, 0), newton(f, 3))

fprime = lambda x: 3*x**2 - 3
print(newton(f, -3, fprime), newton(f, 0, fprime), newton(f, 3, fprime))

from sympy import symbols, N, real_roots