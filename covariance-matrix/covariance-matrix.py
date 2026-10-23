import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    X = np.array(X)
    N = X.shape[0]
    centered_features = X - np.mean(X, axis=0)

    return   (centered_features.T @ centered_features) / (N - 1)