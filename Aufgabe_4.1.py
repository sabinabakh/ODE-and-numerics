"""
Erste Programmieraufgabe
"""

import numpy as np
import matplotlib.pyplot as plt
import math

"""interpoly(x,f) berechnet zu gegebenen Stützpunkten (xj,fj) mit x=[x1,...,xn], f=[f1, ..., fn] das zugehörige 
Interpolationspolynom und plotet im Intervall x ∈[min xj,max xj]. 
"""

def interpoly(x,f):
    
    fig, axes = plt.subplots()
    fig.tight_layout(h_pad=2.5)

    x_new=np.linspace(min(x),max(x),200) 
    
    axes.plot(x_new, polynomial(x,f,x_new),color='black')
    axes.plot(x, f, 'o', markersize=5)
    
    plt.show()
    
    return 'Interpolationspolynomswerte bei x=[x0,x1,...,xn-1]: {}'.format(polynomial(x,f,x))
    

#polynom 

def polynomial(x,f,x_val):
    
    n=len(x)
    
    y_val = 0 # Implementing Lagrange Interpolation
    for i in range(n):
        L = 1 #assigning an initial value to the Lagrange basis 
        for j in range(n):
            if i != j:
                L = L * (x_val - x[j])/(x[i] - x[j])
        y_val += L * f[i] #calculating the polynom 
    return y_val


#x values

n = 16 #n nodes
x =np.linspace(-6, 6, n) # points to interpolate at

#Tschebyscheff-values

x_T=[]
for k in range(1, n+1):
    x_T.append(math.cos(math.pi*(2*k-1)/(2*(n))))
x_T = ((min(x)+max(x))/2)+((max(x)-min(x))/2)*np.array(x_T)


#first function 

def func1(x):
    return math.cos(x)
y1=np.vectorize(func1)
func_1=y1(x) #bei n äquidistante Stützstellen
func_1T=y1(x_T) #bei Tschebyscheff-Stützstellen


#second function 

def func2(x):
    return 1/(1 + x**2)
func_2=np.array(func2(x)) #bei n äquidistante Stützstellen
func_2T=np.array(func2(x_T)) #bei Tschebyscheff-Stützstellen

print(interpoly(x,func_2))

print(interpoly(x_T,func_2T))

print(interpoly(x,func_1))

print(interpoly(x_T,func_1T))

