"""
Task (c)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import svd

fig, axes = plt.subplots(1,4)
fig.tight_layout()

E=np.array([[0, 1, 1, 1.5, 2.5, 3, 3, 4, 2, 2, 1, -3.7, -5, -4, -3, 0], 
            [1, 0, 3.5, 4, 4, 3.5, 3, 3, 2, -1, -2, -2, 1, 0, 1 ,1]])

A=np.array([[1,-0.5],[1,1]])
U,S,V_T= svd(A)

angle = np.linspace( 0 , 2 * np.pi, 150) 
radius = 6
 
x = radius * np.cos( angle ) 
y = radius * np.sin( angle ) 

# subplot 1

X=np.array([x,y])

axes[0].plot(X[0,:],X[1,:], color='black') 
axes[0].set_aspect( 1 ) 

axes[0].set_xticks(np.arange(-10,11,10))
axes[0].set_xticks(np.arange(-10,11,1),minor=True)
axes[0].set_yticks(np.arange(-10,11,5))
axes[0].set_yticks(np.arange(-10,11,1),minor=True)

#axes[0].grid(which='both', alpha=0.2)

axes[0].axis([-10, 10, -10, 10])

axes[0].plot(E[0,:],E[1,:], color='black')

axes[0].set_title("Ausgangsbild",fontsize=9)

# subplot 2

X1=V_T@X
E1=V_T@E

axes[1].plot(X1[0,:],X1[1,:], color='black') 
axes[1].set_aspect( 1 )

axes[1].set_xticks(np.arange(-10,11,10))
axes[1].set_xticks(np.arange(-10,11,1),minor=True)
axes[1].set_yticks(np.arange(-10,11,5))
axes[1].set_yticks(np.arange(-10,11,1),minor=True)

#axes[1].grid(which='both', alpha=0.2)

axes[1].axis([-10, 10, -10, 10])

axes[1].plot(E1[0,:],E1[1,:], color='black')

axes[1].set_title("nach orth.Trafo.V_T",fontsize=9)

# subplot 3

S_diag = np.zeros((2,2))
np.fill_diagonal(S_diag, S)

X2=S_diag@X1
E2=S_diag@E1

axes[2].plot(X2[0,:],X2[1,:], color='black') 
axes[2].set_aspect( 1 )

axes[2].set_xticks(np.arange(-10,11,10))
axes[2].set_xticks(np.arange(-10,11,1),minor=True)
axes[2].set_yticks(np.arange(-10,11,5))
axes[2].set_yticks(np.arange(-10,11,1),minor=True)

#axes[2].grid(which='both', alpha=0.2)

axes[2].axis([-10, 10, -10, 10])

axes[2].plot(E2[0,:],E2[1,:], color='black')

axes[2].set_title("nach Streckung Σ",fontsize=9)

# subplot 4

X3=U@X2
E3=U@E2

axes[3].plot(X3[0,:],X3[1,:], color='black') 
axes[3].set_aspect( 1 )

axes[3].set_xticks(np.arange(-10,11,10))
axes[3].set_xticks(np.arange(-10,11,1),minor=True)
axes[3].set_yticks(np.arange(-10,11,5))
axes[3].set_yticks(np.arange(-10,11,1),minor=True)

#axes[3].grid(which='both', alpha=0.2)

axes[3].axis([-10, 10, -10, 10])

axes[3].plot(E3[0,:],E3[1,:], color='black')

axes[3].set_title("nach orth.Trafo.U", fontsize=9)

#print(svd(A))

plt.show()

#print(U@S_diag@V_T)

