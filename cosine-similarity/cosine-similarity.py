import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.array(a,dtype=float)
    b = np.array(b,dtype=float) 
    if a.ndim!=1 or b.ndim !=1:
        raise TypeError("Dimensions of the 2 arrays are not correct")
    normA = np.linalg.norm(a)
    normB = np.linalg.norm(b)
    if normA== 0.0 or normB ==0.0: return 0.0
     
    norm = (normA*normB)
    res =  float(np.dot(a,b)/norm)
    return res
    pass