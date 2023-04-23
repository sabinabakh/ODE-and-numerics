"""
Dritte Programmieraufgabe
"""

import numpy as np
import matplotlib.pyplot as plt
import math

"""ableitungsplot(f,a,b,n,h) berechnet und plottet die Graphen von f,f',f" im Intervall [a,b]. 

n: Anzahl der Stützpunkte.
"""

def ableitungsplot(f,a,b,n,h): 
    
    x=np.linspace(a,b,n)

    df=(f(x+h)-f(x-h))/2*h #derivative
    d2f=(f(x-h)-2*f(x)+f(x+h))/h**2 #second derivative
    
    fig, axes = plt.subplots()
    fig.tight_layout()

    axes.plot(x, f(x), color='black', label='$f$')
        
    axes.plot(x, df, label='$\u03B4f$')
    axes.plot(x, d2f, color='blue', label='$\u03B4^{2}f$')
    
    axes.legend(loc="upper left")

    plt.show()

    
def func1(x):
    return math.sin(x)
func1=np.vectorize(func1)


def func2(x):
    return x**3

ableitungsplot(func1,-10,10,200,1)
ableitungsplot(func2,-10,10,200,1)
