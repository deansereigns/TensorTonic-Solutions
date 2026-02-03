import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x = np.array(x,dtype=float)
    y = np.array(y,dtype=float)

    # return float((np.sum((x-y)*(x-y))) ** 0.5)

    return np.linalg.norm(x-y)
    pass