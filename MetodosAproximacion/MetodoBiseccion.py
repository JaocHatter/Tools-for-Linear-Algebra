from math import sin
from tabulate import tabulate

def f(x):
    return 25/9 * x**2 - 25

# Parámetros iniciales
tol = 1e-5
a, b = 2, 5
fa = f(a)
fb = f(b)
n = 100
it = 0

# Lista para almacenar los datos de cada iteración
data = []

while abs(a-b) > tol and it < n:
    c = (a + b) / 2
    fc = f(c)

    # Signos para f(a)*f(c) y f(c)*f(b)
    sign_fa_fc = "+" if fa * fc > 0 else "-"
    sign_fc_fb = "+" if fc * fb > 0 else "-"

    if fc == 0:
        a = b = c
    elif fa * fc < 0:
        b = c
        fb = fc
    else:
        a = c
        fa = fc
    # Almacenar los datos de la iteración
    data.append([it, a, b, fa, fb, fc, c, sign_fa_fc, sign_fc_fb])
    it += 1

# Imprimir la tabla con los datos de cada iteración
headers = ["Iteración", "a", "b", "f(a)", "f(b)", "f(c)", "c", "f(a)*f(c)", "f(c)*f(b)"]
print(tabulate(data, headers=headers, tablefmt="grid"))
