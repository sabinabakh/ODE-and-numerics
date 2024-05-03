"""
Task (b)
"""

import numpy as np
import numpy.linalg as lin
from scipy.sparse import diags


def solve_tridiagonal(a,b,f):
    
    n = len(f) # n is the number of rows
    c=np.zeros(n)
    d=np.zeros(n-1)
    y=np.zeros(n)
    u=np.zeros(n)
    
    c[0]=np.sqrt(a[0])
    d[0]=b[0]/c[0]
    
    for i in range(1,n-1):
        c[i]= np.sqrt(a[i]-(d[i-1]**2))
        d[i]=b[i]/c[i]
    c[n-1]= np.sqrt(a[n-1]-(d[n-2]**2))
   
    
    #Forward substitution
    
    y[0]=f[0]/c[0]
    
    for i in range(1,n):
        y[i]=(f[i]-d[i-1]*y[i-1])/c[i]
    
    #Backward substitution
    
    u[n-1]=y[n-1]/c[n-1]

    for i in range(n-2,-1,-1):
        u[i]=(y[i]-u[i+1]*d[i])/c[i]
   
    return u

n=3
a = np.append(2*np.ones(n-1), [1])
b = -1*np.ones(n-1)
f = np.ones(n)

k = [-1*np.ones(n-1),np.append(2*np.ones(n-1), [1]),-1*np.ones(n-1)] # sequence of arrays containing the values 
#on the diagonals, corresponding to offsets
A = diags(k,[-1,0,1]).toarray() #creates tridiagonal matrix and converts it to an array
# offset sets diagonals to: k = 0 the main diagonal (default), k > 0 the kth upper diagonal, 
# k < 0 the kth lower diagonalonal matrix

#print(lin.solve(A,f))
print(solve_tridiagonal(a,b,f))

""" As n increases, the entries of the 
displacement vector u also increase
"""