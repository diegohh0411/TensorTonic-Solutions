import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    centered = x - np.mean(x);
    n = len(x)

    s_squared = np.sum(centered ** 2) / (n - 1)

    return {
        "variance": float(s_squared),
        "standard_deviation": float(np.sqrt(s_squared))
    }