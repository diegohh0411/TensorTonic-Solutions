import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    n = len(A)
    m = len(A[0]) # It's guaranteed that M, N will be at least 1
    
    npa = np.asarray(A)
    output = np.empty((m, n), dtype=float)
    
    
    for i in range(n):
        for j in range(m):
            output[j][i] = npa[i][j]

    return output
