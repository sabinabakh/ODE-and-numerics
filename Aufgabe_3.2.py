#!/usr/bin/env node

"""
Zweite Programmieraufgabe
"""

import numpy as np
from numpy import linalg as la

max_iterations = 10000

"""newton_method(x0,f,f1) berechnet mit Hilfe des Newton-Verfahrens die Gleichgewichtslage x für die Masse m.
"""

def newton_method(x0,f,f1):
    x=x0
    for i in range(max_iterations):
        h=la.solve(f1(x),f(x))
        x=x-h
        if la.norm(f(x))<=tol:
            break
    return x

def f(x):
    return f_1(x)+f_2(x)+G
def f_1(x):
    return s1*(l1/la.norm(x-a1)-1)*(x-a1)
def f_2(x):
    return s2*(l2/la.norm(x-a2)-1)*(x-a2)
    
def f1(x): 
    return f1_1(x)+f1_2(x)
def f1_1(x): #Ableitung von f(x)
    return s1*((l1/la.norm(x-a1)-1)*np.identity(2)-l1*(x-a1)*(x-a1).T/la.norm(x-a1)**3)
def f1_2(x): #Ableitung von f(x)
    return s2*((l2/la.norm(x-a2)-1)*np.identity(2)-l2*(x-a2)*(x-a2).T/la.norm(x-a2)**3)



a1=np.array([0,0]).reshape(2,1) #Punkt an dem, die Feder1 befestigt ist
a2=np.array([1,1]).reshape(2,1) #Punkt an dem, die Feder2 befestigt ist
s1=10 #Steifigkeit s>0 der Feder1
s2=10 #Steifigkeit s>0 der Feder2
l1=2 #Länge l>0 der Feder1 im entspannten Zustand 
l2=2 #Länge l>0 der Feder2 im entspannten Zustand
m=1 #Masse, die an zwei Federn aufgehängt ist
G=np.array([0,-9.81*m]).reshape(2,1) #Gewichtskraft
tol=10**(-7)

x01=np.array([0,-4]).reshape(2,1)
x02=np.array([0,4]).reshape(2,1)

print(newton_method(x01,f,f1))
print(newton_method(x02,f,f1))

"""Die Ergebnisse sind unterschiedlich, weil f mehr als nur eine Nullstelle haben kann. Abhängig von dem Startwert können wir verschiedene Nullstellen bekommen.
"""
