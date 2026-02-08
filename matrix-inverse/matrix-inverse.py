import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    A = np.array(A, dtype=float)
    if A.ndim != 2:
        return None

    n, m = A.shape
    if n != m:
        return None

    det = np.linalg.det(A)
    if abs(det) < 1e-10:
        return None

    A_inv = np.linalg.inv(A)
    return A_inv