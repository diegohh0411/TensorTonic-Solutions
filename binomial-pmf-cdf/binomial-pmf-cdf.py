import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """

    pmf = math.comb(n, k) * math.pow(p, k) * math.pow(1.0 - p, n - k)
    cdf = 0;
    for i in range(0, k):
        cdf += math.comb(n, i) * math.pow(p, i) * math.pow(1.0 - p, n - i)
    cdf += pmf # Re-using it, to avoid calculating it twice
    
    return {
        "pmf": float(pmf),
        "cdf": float(cdf)
    }

    