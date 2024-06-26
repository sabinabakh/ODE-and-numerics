import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import math

"""integral(f, a, b, n) calculates the integral of f using the trapezoidal rule (result T) and Simpson's rule (result S).

n: the number of support points.
h = (b-a)/(n-1): interval length.
"""
def integral(f, a, b, n):
    
    # Trapezoidal rule 
    
    x = np.linspace(a, b, n)
    h = (b - a) / (n - 1)
    
    a1 = a
    y = 0
    for i in range(n - 1):
        y += f(a1) + f(a1 + h)
        a1 += h
        
    T = (h / 2) * y  
        
    # Simpson's rule

    start = f(a)
    finish = f(b)
    
    x_ = 0
    value = 0
    
    for i in range(1, n - 1):
        x_ = a + i * h
        value_ = f(x_)
    
        if i % 2 == 0:
            value += 2 * value_
        else:
            value += 4 * value_
        
    total = (h / 3) * (start + value + finish)

    S = total
    
    # Tests

    # print('Expected output: ({},{},)'.format(np.trapz(f(x), x), integrate.simpson(f(x), x)))

    return T, S
    
def func1(x):
    return math.sin(x)
func1 = np.vectorize(func1)


def func2(x):
    return x**3

print(integral(func1, -10, 100, 101))
print(integral(func2, -10, 100, 101))
