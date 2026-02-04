import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    mean = float(np.mean(x))
    median = float(np.median(x))

    freq = Counter(x)
    max_freq = max(freq.values())
    mode = float(min(x for x, c in freq.items() if c == max_freq))

    return mean, median, mode