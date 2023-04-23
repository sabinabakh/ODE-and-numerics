"""
Aufgabe (a)
"""

import numpy as np
from scipy.linalg import hilbert
import numpy.linalg as lin
from scipy.linalg import lu

#Zahlen
z=np.array((12,1))
z=np.array([[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13]], dtype='O')
n=12

#Konditionszahlen der Hilbertmatrizen der Dimensionen n = 2, 3, . . . , 13 bezüglich der ∞-Norm
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
    
    #relativer Fehler, wobei x_bs die numerische Lösung von Ax = b
    x_bs=lin.solve(A,b)
    f_bs=np.linalg.norm(x-x_bs, np.inf)/np.linalg.norm(x, np.inf)
    f1[i-2]=np.array(f_bs)
    
    #relativer Fehler, wobei x_lr die numerische Lösung von Ax = b mit LR-Zerlegung
    P,L,R =lu(A)
    y=lin.solve(P@L,b)
    x_lr=lin.solve(R, y)
    
    f_lr=np.linalg.norm(x-x_lr, np.inf)/np.linalg.norm(x, np.inf)
    f2[i-2]=np.array(f_lr)

    #relativer Fehler, wobei x_chol die numerische Lösung von Ax = b mit Cholesky- Zerlegung
    L = np.linalg.cholesky(A)
    y=lin.solve(L,b)
    x_chol=lin.solve(L.T,y)
    
    f_chol=np.linalg.norm(x-x_chol, np.inf)/np.linalg.norm(x, np.inf)
    f3[i-2]=np.array(f_chol)
    
    #Probewert
    p[i-2]=np.linalg.norm(A*x_chol-b, np.inf)
    
T1=np.hstack([z, c, f1, f2, f3, p])

print(T1)

""" Die Algorithmen zur Bestimmung der nummerischen Lösung von Ax = b 
mit Hilfe der LR-Zerlegung (mit dem relatinen Fehler f2) und direkt aus der Gleichung Ax=b (mit dem relatinen 
Fehler f1) schneiden am schlechtestens ab. Die relativen Fehlerwerte bei diesen Algorithmen sind identisch.

Alle Hilbert Matrizen sind positiv definit. Wenn man aber die Tabelle bis n = 14 oder n = 15 erstellt, 
bekommen wir dann die Fehlermeldung: "raise LinAlgError("Matrix is not positive definite")". 
Dann kann also die Cholesky-Zerlegung der matrix nicht berechnet werden.

Behauptung: der Grund dafür kann in Python der Fehler bei der Berechnung (der Hilbert Matrix (?)) sein, da je 
größer die Dimmension ist, desto größer ist der Fehler.
"""

""" Function that shows if a matrix is positive definite:

def pos_def(x): 
    return np.all(np.linalg.eigvals(x) > 0) #computes the eigenvalues of a general matrix and 
    #tests whether all array elements (all eigenvalues) evaluate to True.
 
pos_def(hilbert(14))
"""