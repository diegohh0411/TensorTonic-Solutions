import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    if norm_type == "l1":
        sum_norms = np.sum(np.abs(matrix), axis=axis, keepdims=True) # First, we get the total sum of the row/column according to the axis
        return matrix / np.where(sum_norms == 0, 1, sum_norms)
    elif norm_type == "l2":
        euclidean_norms = np.sqrt(np.sum(np.square(matrix), axis=axis, keepdims=True))
        return matrix / np.where(euclidean_norms == 0, 1, euclidean_norms)
    elif norm_type == "max":
        max_norms = np.max(np.abs(matrix), axis=axis, keepdims=True)
        return  matrix / np.where(max_norms == 0, 1, max_norms)
    