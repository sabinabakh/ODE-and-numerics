"""
Erste Programmieraufgabe
"""

"""loeservergleich(h) löst Anfangsproblem im Intervall [0,50] mit dem expliziten Eulerverfahren, dem 
Collatzverfahren und dem Heunverfahre und die Lösungen in ein Diagramm plottet.
"""

import numpy as np
from matplotlib import pyplot as plt

"""initial value problem
"""
def loeservergleich(h):
        
    #initial condition
    
    t0=0
    y0=1
    
    tf=50
    n=round((tf-t0)/h)+1 #size of t vector 
        
    t=np.linspace(0,50,n)
    
    #Explicit Euler method
        
    y1 = np. zeros ([n])
    y1[0]=y0
    for i in range(1,n):
        y1[i] = y1[i-1]+h*(np.cos(t[i-1])*y1[i-1])
        
    #Collatz method
    
    y2 = np. zeros ([n])
    y2[0]=y0
    for i in range(1,n):
        y2[i] = y2[i-1]+h*(np.cos(t[i-1]+h/2)*(y2[i-1]+(h/2)*np.cos(t[i-1])*y2[i-1]))
    
    #Heun method
    
    y3 = np. zeros ([n])
    y3[0]=y0
    for i in range(1,n):
        y3[i] = y3[i-1]+h*((np.cos(t[i-1])*y3[i-1])+(np.cos(t[i-1]+h)*(y3[i-1]+h*np.cos(t[i-1])*y3[i-1])))/2
            
    #plot
    
    fig, axes = plt.subplots()
    fig.tight_layout()
    
    axes.plot(t, y1, label='explicit Euler method')
    axes.plot(t, y2, label='Collatz method')
    axes.plot(t, y3, label='Heun method')
    
    axes.legend(loc="best", prop={'size': 6})

    
    plt.show()
    
    return ' '
                
for i in [0.5,0.2,0.1,0.01]:
    print(loeservergleich(i))    