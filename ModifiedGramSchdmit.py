import numpy as np

def gram_schmidt(A):
    n = A.shape[1]
    Q = np.zeros_like(A)
    R = np.zeros((n, n))

    for k in range(n):
        R[k, k] = np.linalg.norm(A[:, k])
        Q[:, k] = A[:, k] / R[k, k]
        for j in range(k+1, n):
            R[k, j] = np.dot(Q[:, k], A[:, j])
            A[:, j] = A[:, j] - R[k, j] * Q[:, k]
        
        print(f"Iteration {k+1}:")
        print(f"Vector a_{k+1} normalized (q_{k+1}): {Q[:, k]}")
        print(f"Residual matrix R so far:\n{R[:k+1, :k+1]}")
        print("-------------------------------------------------")
    
    return Q, R

# Ejemplo con vectores aleatorios
A = np.array([[2,1,0],[1,1,0],[2,1,0]],dtype='f4')  # Reemplazar con vectores específicos si es necesario
Q, R = gram_schmidt(A)

print("Vectores ortonormalizados:")
print(Q)
