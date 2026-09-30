from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    npx = np.asarray(x)

    counts = Counter(npx)

    top_count = counts.most_common(1)[0][1] # This is the number of times that all modes appear in the list

    modes = [
        item for item, count in counts.items() if count == top_count
    ]

    modes = sorted(modes)
    
    return {
        "mean": float(np.mean(npx)),
        "median": float(np.median(npx)),
        "mode": float(modes[0])
    }