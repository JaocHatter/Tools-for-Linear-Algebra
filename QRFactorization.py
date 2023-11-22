import numpy as np

def gram_schmidt_verbose(A):
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    for i in range(n):
        print("------------------------------------------")
        print(f"Procesando vector columna {i+1} de A:")
        print("------------------------------------------")
        v = A[:, i]
        print(f"v_{i+1} original: {v}")
        
        for j in range(i):
            q = Q[:, j]
            R[j, i] = q @ v
            v = v - R[j, i] * q
            print(f"Proyectando v_{i+1} sobre q_{j+1} y restando la proyección: {v}")
            
        R[i, i] = np.linalg.norm(v)
        Q[:, i] = v / R[i, i]
        print(f"Vector ortogonalizado u_{i+1} antes de normalizar: {v}")
        print(f"Vector normalizado q_{i+1}: {Q[:, i]}")
        print(f"Matriz R parcialmente construida:\n{R[:i+1, :i+1]}")
        
    return Q, R


# Ejemplo de uso:
A = np.array([[2, 1, -1],
              [1, 0, 2],
              [2, -1, 3]],dtype='f4')
Q, R = gram_schmidt_verbose(A)

print("Q (ortogonal):")
print(Q)
print("\nR (triangular superior):")
print(R)
