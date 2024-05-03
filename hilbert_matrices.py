"""
Task (a)
"""

import numpy as np
from scipy.linalg import hilbert
import numpy.linalg as lin
from scipy.linalg import lu

# Numbers
z=np.array((12,1))
z=np.array([[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13]], dtype='O')
n=12

# Condition numbers of Hilbert matrices of dimensions n = 2, 3,..., 13 with respect to the infinity norm
c=np.zeros((12,1))
for i in range(0,n):
    A=hilbert(i+2)
    c[i]=np.linalg.cond(A, np.inf)*10**(-16) 

n=13

f1=np.zeros((12,1))
f2=np.zeros((12,1))
f3=np.zeros((12,1))
p=np.zeros((12,1))

for i in range(2,n+1):
    x=np.zeros(i)
    
    x[0]=1
    x[i-1]=1
   
    A=hilbert(i)
    b=A[:,0]+A[:,i-1]
    
    # Relative error, where x_bs is the numerical solution of Ax = b
    x_bs=lin.solve(A,b)
    f_bs=np.linalg.norm(x-x_bs, np.inf)/np.linalg.norm(x, np.inf)
    f1[i-2]=np.array(f_bs)
    
    # Relative error, where x_lr is the numerical solution of Ax = b using LU decomposition
    P,L,R =lu(A)
    y=lin.solve(P@L,b)
    x_lr=lin.solve(R, y)
    
    f_lr=np.linalg.norm(x-x_lr, np.inf)/np.linalg.norm(x, np.inf)
    f2[i-2]=np.array(f_lr)

    # Relative error, where x_chol is the numerical solution of Ax = b using Cholesky decomposition
    L = np.linalg.cholesky(A)
    y=lin.solve(L,b)
    x_chol=lin.solve(L.T,y)
    
    f_chol=np.linalg.norm(x-x_chol, np.inf)/np.linalg.norm(x, np.inf)
    f3[i-2]=np.array(f_chol)
    
    # Test value
    p[i-2]=np.linalg.norm(A*x_chol-b, np.inf)
    
T1=np.hstack([z, c, f1, f2, f3, p])

print(T1)

"""
The algorithms for determining the numerical solution of Ax = b using LU decomposition (with relative error f2) 
and directly from the equation Ax = b (with relative error f1) perform the worst. The relative error values for 
these algorithms are identical.

All Hilbert matrices are positive definite. However, when creating the table up to n = 14 or n = 15, we get the 
error message: "raise LinAlgError('Matrix is not positive definite')". Then the Cholesky decomposition of the 
matrix cannot be calculated.

Hypothesis: The reason for this can be in Python the error in the calculation (of the Hilbert matrix?). As the 
dimension increases, the error also increases.
"""

""" Function that checks if a matrix is positive definite:

def is_positive_definite(x): 
    return np.all(np.linalg.eigvals(x) > 0) # Computes the eigenvalues of a general matrix and 
    # tests whether all array elements (all eigenvalues) evaluate to True.
 
is_positive_definite(hilbert(14))
"""