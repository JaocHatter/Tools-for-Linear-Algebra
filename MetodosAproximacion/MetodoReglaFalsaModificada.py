from math import sin
from tabulate import tabulate

def f(x):
    return 25/9 * x**2 - 25

# Parámetros iniciales
tol = 1e-5
a, b = 2, 5
fa = f(a)
fb = f(b)
it = 0
a_old, b_old = a, b

# Lista para almacenar los datos de cada iteración
data = []

# Verificamos que hay un cambio de signo
if fa * fb > 0:
    print("La función debe tener signos opuestos en a y b para aplicar el método.")
else:
    # Iniciamos el método de la regla falsa modificada
    while (b - a) / 2 > tol:
        if fa==fb:
            break
        c = b - (fb * (a - b)) / (fa - fb)
        fc = f(c)
        if abs(fc)<tol:
            break
        # Signos para f(a)*f(c) y f(c)*f(b)
        sign_fa_fc = "+" if fa * fc > 0 else "-"
        sign_fc_fb = "+" if fc * fb > 0 else "-"

        # Verificar si se divide fa o fb
        divide_fa_fb = "fa/2" if it > 1 and f(b) == f(b_old) else ("fb/2" if it > 1 and f(a) == f(a_old) else "No")

        # Almacenar los datos de la iteración
        data.append([it, a, b, fa, fb, fc, c, sign_fa_fc, sign_fc_fb, divide_fa_fb])

        # Aplicar la regla falsa modificada
        if fa * fc < 0:
            b, fb = c, fc
            if it > 1 and f(b) == f(b_old):
                fa /= 2
        else:
            a, fa = c, fc
            if it > 1 and f(a) == f(a_old):
                fb /= 2
        # Almacenar valores antiguos
        a_old, b_old = a, b
        it += 1

# Imprimir la tabla con los datos de cada iteración
headers = ["Iteración", "a", "b", "f(a)", "f(b)", "f(c)", "c", "f(a)*f(c)", "f(c)*f(b)", "Divide fa/fb"]
print(tabulate(data, headers=headers, tablefmt="grid"))
