#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

"""
Aufgabe (a)
"""

"""
vorrueck(L,R,b) löst das Gleichungssystem LRx = b durch Vorwärts- und Rückwärtseinsetzen
L ist eine untere Dreiecksmatrix in R^nxn
R ist eine obere Dreiecksmatrix in R^nxn 
b ist eine Vektor in R^n
@param: L, R, b
@return: x
"""
def vorrueck(L,R,b):
    
    y=vorwaert(L,b)
    x=rueck(R,y)
    return x

"""
vorwaert(L,b) löst das Gleichungssystem Ly = b durch Vorwärtseinsetzen
L ist eine untere Dreiecksmatrix in R^nxn 
b ist eine Vektor in R^n
@param: L, b
@return: y
"""
def vorwaert(L,b):
    
    n=len(b)
    y=np.eye(n,1)
    
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i,j] * y[j]
        y[i] = y[i] / L[i,i]
        
        y=np.array(y)
       
    return y

"""
rueck(R,y) löst das Gleichungssystem Rx= y durch Rückwärtseinsetzen
R ist eine untere Dreiecksmatrix in R^nxn
y ist eine Vektor in R^n
@param: R, y
@return: x
"""
def rueck(R,y):
    
    n=len(y)
    x=np.eye(n,1)
    
    for i in range(n-1, -1, -1):
        x[i] = y[i]
        for j in range(i+1, n):
            x[i] -= R[i,j] * x[j]
        x[i] = x[i] / R[i,i]
        
    return x

"""
Aufgabe (b)
"""

"""
[L,R]=lr(A) berechnet die LR-Zerlegung der Matrix A in R^nxn ohne Pivotisierung
A ist eine Matrix in R^nxn
@param: A
@return: L, R
"""
def lr(A):
    
    n=len(A)
    L=np.eye(n,n) #Eine Einheitsmatrix erstellen 
    R=A.astype('float') #copies A into R
    
    for i in range(n-1):
        for j in range(i+1,n):
            L[j,i] = R[j,i]/R[i,i]
            R[j,i:] = R[j,i:]-L[j,i]*R[i,i:]

    return L, R

"""
Tests 
"""

#y=np.array([[18, 33, -6]])
    
L=np.array([[1,0,0],[-2,1,0],[4,5,1]])
R=np.array([[2,-1,6],[0,3,9],[0,0,-2]])
b=np.array([18,-3,231])

A=L@R

#print(vorwaert(L,b))
print(vorrueck(L,R,b))

print(lr(A))
#print(np.allclose(lr(A), (L,R)))

#print(L)
#print(R)

