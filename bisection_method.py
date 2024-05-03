#!/usr/bin/env node

import numpy as np
import matplotlib.pyplot as plt
import math

max_iterations = 10000

"""bisection_method(f,a,b,tol) calculates a root of the function f in the interval [a,b] using the Bisection Method.
"""

def bisection_method(f,a,b,tol): ##Choose a and b close to 
    #the root c,
    #so that a<b and f(a) and f(b) have different signs
   
    if f(a)*f(b)<0: 
        
        for i in range(max_iterations): 
            if abs(a-b)>tol:
                c=(a*f(b)-b*f(a))/(f(b)-f(a))
                a=c 
                
                if f(c) == 0: 
                    break
                
                elif f(c)*f(a)< 0: 
                    b = c 
                else: 
                    a = c 

    else:
        return "a and b are not chosen correctly"
    
    return round(c,10)
  
def f(x): #function f
    return (1 + math.cos(x)*math.cosh(x))

fig = plt.figure()

x=np.linspace(0,4,100)  
y=np.vectorize(f)

plt.plot(x, y(x), color='black')
plt.grid(which='both', alpha=0.3)
plt.ticklabel_format(useOffset = False)

print(bisection_method(y,1,3,0.001))

plt.show()

