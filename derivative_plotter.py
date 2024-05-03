#!/usr/bin/env python3

"""
Third Programming Task
"""

import numpy as np
import matplotlib.pyplot as plt
import math

"""derivative_plot(f, a, b, n, h) calculates and plots the graphs of f, f', f" in the interval [a, b].

n: number of support points.
"""

def derivative_plot(f, a, b, n, h): 
    
    x = np.linspace(a, b, n)

    df = (f(x + h) - f(x - h)) / (2 * h) # first derivative
    d2f = (f(x - h) - 2 * f(x) + f(x + h)) / (h ** 2) # second derivative
    
    fig, axes = plt.subplots()
    fig.tight_layout()

    axes.plot(x, f(x), color='black', label='$f$')
        
    axes.plot(x, df, label='$\delta f$')
    axes.plot(x, d2f, color='blue', label='$\delta^{2} f$')
    
    axes.legend(loc="upper left")

    plt.show()

    
def func1(x):
    return math.sin(x)
func1 = np.vectorize(func1)


def func2(x):
    return x ** 3

derivative_plot(func1, -10, 10, 200, 1)
derivative_plot(func2, -10, 10, 200, 1)
