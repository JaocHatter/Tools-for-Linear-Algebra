import numpy as np
from tabulate import tabulate

# Definimos g(x) basándonos en f(x)
def g(x):
    return 4 + (1/3)*np.sin(2*x)

def punto_fijo(g, x0, tol, max_iter):
    x_k = x0
    data = []  # Lista para almacenar los datos de cada iteración

    for k in range(max_iter):
        x_next = g(x_k)

        # Almacenar los datos de la iteración
        data.append([k, x_k, x_next, abs(x_next - x_k)])

        if abs(x_next - x_k) < tol:
            break

        x_k = x_next

    # Imprimir la tabla con los datos de cada iteración
    headers = ["Iteración", "x_k", "x_(k+1)", "Error"]
    print(tabulate(data, headers=headers, tablefmt="grid"))

    return x_k

x0 = 0  # Valor inicial
tol = 1e-5  # Tolerancia
max_iter = 100  # Número máximo de iteraciones

solucion = punto_fijo(g, x0, tol, max_iter)
print("Solución aproximada:", solucion)
