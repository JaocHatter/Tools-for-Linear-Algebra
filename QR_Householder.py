import numpy as np
    
def QR_householder(A):
    m, n = A.shape
    aux = np.copy(A)
    Q = np.eye(m)
    print("\n =>  Factorización QR - Transformaciones House-Holder")

    for k in range(n):
        print("------------------------------ Iteracion k =", k + 1, "----------------------------------")
        v = np.copy(aux[0:, 0])
        a = v
        v[0] += np.sign(v[0]) * np.linalg.norm(v)
        print(f"a_{k+1}:", a, f"\tv_{k+1}:", v)

        v = v / np.linalg.norm(v)

        auxH = np.eye(m - k) - 2.0 * np.outer(v, v)
        
        H = np.eye(m)
        H[k:, k:] = auxH
        print(f"H_{k+1}:\n", H)

        aux = auxH @ aux
        print(f"A_{k+1}:\n", aux)

        aux = aux[1:, 1:]

        Q = Q @ H
        
        print()
    
    R = Q.T @ A
    print("---------------------------------------------------------------------------------\n")
    return Q, R


# ----------------------------------------------
print("=> DATOS DEL PROBLEMA")
A = np.array([[2, -2, 18],
              [2, 1, 0],
              [1, 2, 0]],dtype='f4')

b = np.array([1, 1, 1],dtype='f4')

r = np.linalg.matrix_rank(A)

print("Matriz A: => ran(A) =", r )
print(A)
print("Vector de coeficientes b: ")
print(b)


Q,R = QR_householder(A)

print("Matrices Resultantes de la Factorizacion QR")
print("Q = H_1.H_2.H_3 =")
print(Q)
print("\nR = H_3.H_2.H_1.(A) =")
print(R)
c = np.transpose(Q) @ b
print("\nSistema Resultante: R x = Q^t b")
print("Q^t b = c = ", c)
print("Resolviendo el sistema se tiene  x = ", np.linalg.solve(R,c))
