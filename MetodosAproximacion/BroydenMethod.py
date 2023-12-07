# Continuación del código de broyden...
from numpy import dot, sqrt, array, eye
from numpy.linalg import solve
import numpy as np
def  broyden(x0,A0):
    TOL=1e-5
    MAXITER=100
    k=0
    xk=x0
    Ak=A0
    terminar=False
    while not terminar:
        fk=f(xk)
        absfk = sqrt(dot(fk.T,fk))
        if absfk<TOL or k>MAXITER:
            terminar=True
        else:
            sk = solve(Ak,-fk)
            xk1 = xk + sk
            fk1=f(xk1)
            yk = fk1 - fk
            Ak += (1/dot(sk.T,sk)) * (yk - Ak@sk)@sk.T
            xk = xk1
            fk=fk1    
            k += 1
        print(f"k: {k}, xk: {xk}, f(xk): {fk}")
    print(f"Método termino en {k} iteraciones, f(x)={absfk}")
    return xk

from numpy import dot, sqrt, array, eye
from numpy.linalg import solve
from numpy import zeros_like, cos, sin, exp, diag

def f(x):
    z = zeros_like(x)
    z[0] = x[0]*x[1]-42
    z[1] = (x[0]+5)*(x[1]+5)-132
    return z

x0 = array([3,4],dtype=np.float64).T
A0 = array([[4,3],[9,0]],dtype=np.float64)
xk = broyden(x0, A0)

