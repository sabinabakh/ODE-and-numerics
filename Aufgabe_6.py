import numpy as np
from matplotlib import pyplot as plt
from numpy import linalg as la
import math


def graph(t,p,mu,start):
    
    w=mu/1j

    #Graph
    fig, axes = plt.subplots(2,1)
    fig.tight_layout()
    
    #z=0
    axes[0].plot(t, solve_lin_high_order_ode(t,p,0,mu,start).real, color='blue')
    axes[0].set_title('z=0')  
    
    #z=1
    axes[1].plot(t, solve_lin_high_order_ode(t,p,1,mu,start).real, color='blue')
    axes[1].plot(t, func1(w*t), color='red')
    axes[1].set_title('z=1') 

    plt.show()

def solve_lin_high_order_ode(t,p,z,mu,start): #löst DGL

    #find roots of a polynomial 
    poly=np.poly1d(p) 
    roots=np.roots(p)
    
    start=np.array(start)
    mu1=np.array([mu**i for i in range(len(start))])
    
    #matrix A
    A=np.array([[i**j for i in roots] for j in range(len(start))])
    b=start-(z/poly(mu))*mu1
    
    #find coefficients 
    c=la.solve(A,b)
    
    #find y
    
    y_p=(z/poly(mu))*np.exp(mu*t)
    y_h=0
    
    for i in range(len(roots)):
        y_h+=np.exp(roots[i]*t)*c[i] 
    
    y=y_p+y_h

    return y
    
def func1(x): 
    return np.cos(x)    
    

"""Tests
"""

print(graph(np.linspace(0,50,1000),[1,1],2j,[1]))
print(graph(np.linspace(0,50,1000),[2,1,10],1j,[1,0]))
print(graph(np.linspace(0,200,1000),[1,0,4],2.1j,[1,0]))
print(graph(np.linspace(0,100,1000),[1,0.1,17,1,16],1j,[0,0,0,1]))
