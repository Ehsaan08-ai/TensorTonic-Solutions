import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    n, m = A.shape
    Arr = np.zeros((m,n), dtype=A.dtype)
    for i in range(n):
        for j in range(m):
            Arr[j,i] = A[i,j]
    return Arr