import sympy as sp
import numpy as np
from tabulate import tabulate

x, y = sp.symbols('x y')
f1 = x**2 + y**2 - 25
f2 = x - (3/4) * y
F = sp.Matrix([f1, f2])

# Calcular la Jacobiana
J = F.jacobian([x, y])

def evaluar(J, F, valores):
    J_eval = J.subs(valores)
    F_eval = F.subs(valores)
    return np.array(J_eval).astype(np.float64), np.array(F_eval,dtype=np.float32)

# Método de Newton modificado
def newton_method(F, J, x0, tol):
    k = 0
    x_k = np.array(x0, dtype=float)
    data = []  # Lista para almacenar los datos de cada iteración

    while True:
        valores = {x: x_k[0], y: x_k[1]}
        J_eval, F_eval = evaluar(J, F, valores)
        
        h_k = np.linalg.solve(J_eval, -F_eval)
        x_k = x_k + h_k.T[0]

        # Almacenar los datos de la iteración
        data.append([k,x_k[0], x_k[1], h_k[0], h_k[1]])

        if np.linalg.norm(h_k) < tol:
            break
            
        k += 1

    # Imprimir la tabla con los datos de cada iteración
    headers = ["it","x1", "x2", "h1", "h2"]
    print(tabulate(data, headers=headers, tablefmt="grid"))

    return x_k

x0 = [1, 1]  # Vector inicial
tol = 1e-5   # Tolerancia

solucion = newton_method(F, J, x0, tol)
print("Solución:", solucion)
