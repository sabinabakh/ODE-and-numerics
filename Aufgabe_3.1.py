#!/usr/bin/env node

"""
Erste Programmieraufgabe
"""

import numpy as np
import matplotlib.pyplot as plt
import math

max_iterations = 10000

"""regulafalsi(f,a,b,tol) berechnet eine Nullstelle der Funktion f im Intervall [a,b] mit der Regula Falsi.
"""

def regulafalsi(f,a,b,tol): #Wähle a und b nah dran zu 
    #der Nullstelle c,
    #so dass a<b und f(a) und f(b) verschiedenes Vorzeichen haben  
   
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
        return "a unb b sind falsch gewählt"
    
    return round(c,10)
  
def f(x): #funktion f
    return (1 + math.cos(x)*math.cosh(x))

fig = plt.figure()

x=np.linspace(0,4,100)  
y=np.vectorize(f)

plt.plot(x, y(x), color='black')
plt.grid(which='both', alpha=0.3)
plt.ticklabel_format(useOffset = False)

print(regulafalsi(y,1,3,0.001))

plt.show()

