import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    A = np.array(A,dtype=float)
    if len(A) != len(A[0]):
        raise TypeError("Not a Square Matrix")
    if len(A) ==1 and len(A[0])==1: 
        return A[0][0]
    
    n = len(A)
    trace =0.0
    for i in range(n):
        trace+= A[i][i]

    return trace
    pass
