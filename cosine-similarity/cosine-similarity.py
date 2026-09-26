import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    npa = np.asarray(a, dtype=float)
    npb = np.asarray(b, dtype=float)

    dotproduct = np.dot(npa, npb)
    denom = np.linalg.norm(npa) * np.linalg.norm(npb)
    

    return 0.0 if denom == 0 else float(dotproduct / denom)