import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    npx = np.asarray(x, dtype=float)
    npy = np.asarray(y, dtype=float)
    
    return float(np.dot(npx, npy))