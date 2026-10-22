import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    pmf = np.where(np.array(x) == 1, p, 1.0 - p)
    mean = np.mean(pmf)

    return {
        "pmf": pmf,
        "mean": float(p),
        "variance": p *  ( 1.0 - p)
    }