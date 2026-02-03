import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.array(A)
    m = len(A)
    n = len(A[0])
    T = np.zeros((n,m),dtype =float)
    for i in range(n):
        for j in range(m):
            T[i][j] = A[j][i]
    return T
    pass
