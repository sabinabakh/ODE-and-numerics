import numpy as np

"""
Task (a)
"""

"""
solve_linear_system(L,R,b) solves the system of linear equations LRx = b using forward and backward substitution
L is a lower triangular matrix in R^nxn
R is an upper triangular matrix in R^nxn 
b is a vector in R^n
@param: L, R, b
@return: x
"""
def solve_linear_system(L, R, b):
    y = forward_substitution(L, b)
    x = backward_substitution(R, y)
    return x

"""
forward_substitution(L,b) solves the system of linear equations Ly = b using forward substitution
L is a lower triangular matrix in R^nxn 
b is a vector in R^n
@param: L, b
@return: y
"""
def forward_substitution(L, b):
    n = len(b)
    y = np.eye(n, 1)
    
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i, j] * y[j]
        y[i] = y[i] / L[i, i]
        
        y = np.array(y)
       
    return y

"""
backward_substitution(R,y) solves the system of linear equations Rx = y using backward substitution
R is an upper triangular matrix in R^nxn
y is a vector in R^n
@param: R, y
@return: x
"""
def backward_substitution(R, y):
    n = len(y)
    x = np.eye(n, 1)
    
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= R[i, j] * x[j]
        x[i] = x[i] / R[i, i]
        
    return x

"""
Task (b)
"""

"""
[L,R]=calculate_lr_decomposition(A) calculates the LR decomposition of matrix A in R^nxn without pivoting
A is a matrix in R^nxn
@param: A
@return: L, R
"""
def calculate_lr_decomposition(A):
    n = len(A)
    L = np.eye(n, n)  # Create an identity matrix
    R = A.astype('float')  # Copy A into R
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            L[j, i] = R[j, i] / R[i, i]
            R[j, i:] = R[j, i:] - L[j, i] * R[i, i:]

    return L, R

"""
Tests 
"""

L = np.array([[1, 0, 0], [-2, 1, 0], [4, 5, 1]])
R = np.array([[2, -1, 6], [0, 3, 9], [0, 0, -2]])
b = np.array([18, -3, 231])

A = L @ R

print(solve_linear_system(L, R, b))
print(calculate_lr_decomposition(A))