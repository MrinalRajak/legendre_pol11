
#legendre polynomial
#(11) integrate(-1 -->1)((1-x^2)*P'(m,x)*P'(n,x)) = (2*n*(n+1))/(2*n+1)

import numpy as np
from scipy.special import legendre
from scipy.misc import derivative
from scipy.integrate import quad

def f(x):
    return (legendre(m)(x))
def g(x):
    return (legendre(n)(x))

x=float(input("Enter the x: "))
m=int(input("Enter the m: "))
n=int(input("Enter the n: "))
def k(x):
    return (1-x**2)*(derivative(f,x,order=15))*(derivative(g,x,order=15))
LHS= quad(k,-1,1)[0]
RHS= (2*n*(n+1))/(2*n+1.)
if(m==n):
    RHS=(2*n*(n+1))/(2*n+1.)
    print("LHS: ",LHS)
    print("RHS: ",RHS)
elif(m!=n):
    RHS= 0.0
    print("LHS: ",LHS)
    print("RHS: ",RHS)
