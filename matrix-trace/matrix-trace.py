import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    n = A.shape[0]
    total = 0

    for i in range(n):
        total += A[i, i]

    return total