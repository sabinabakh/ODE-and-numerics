#!/usr/bin/env node

"""
Zweite Programmieraufgabe
"""

import numpy as np

"""polyzeros(a) berechnet die Nullstellen eines gegebenen Polynoms p mit Koeffizienten a=[a1, a2...an+1]
"""

def polyzeros(a):
            
    max_iterations = 10000
    
    z=[]

    x=np.random.rand()+1.j*np.random.rand()

    for i in range(max_iterations):
        
        p=np.polyval(a, x) #Evaluate a polynomial at specific values.
        
        a_=np.polyder(np.poly1d(a)) #np.polyder(a) return the derivative of the specified order of a polynomial
        #np.poly1d(a) returns a polynom with coefficients a 
        
        p_=np.polyval(a_, x)
        
        if p_!=0:
            x=x-(p/p_)
            if  abs(p)<=10**(-7):
                break

    z.append(x)     
    
    x=np.random.rand()+1.j*np.random.rand()
    
    max_iterations = 10000
       
    for i in range(max_iterations):
        
        if (x not in z)==True:
            
            if len(z)==len(np.poly1d(a)):
                break
        
            p=np.polyval(a, x) #Evaluates a polynomial at specific values.
        
            a_=np.polyder(np.poly1d(a)) #np.polyder(a) returns the derivative of the specified order of a polynomial
            #np.poly1d(a) returns a polynom with coefficients a 
        
            p_=np.polyval(a_, x)
         
            q=np.poly1d([1,-z[0]])
          
            for i in range(1,len(z)):
                q*=np.poly1d([1,-z[i]])
    
            q_=np.polyder(q)
            qq_=np.polyval(q_, x)
            qq=np.polyval(q, x)
        
            if p!=0 and qq!=0:
                x=x-(1/((p_/p)-(qq_/qq)))
         
            if  abs(p)<=10**(-7):
                z.append(x)
                x=np.random.rand()+1.j*np.random.rand()  


              
    return z

a=[1,0,0,0,-1]

p=np.poly1d(a)

#print(p)
#print('')

#Tests

print('Erwatete Nullstellen: {}'.format(np.roots(a)))
print('')

print('Berechnete Nullstellen: {}'.format(polyzeros(a)))
