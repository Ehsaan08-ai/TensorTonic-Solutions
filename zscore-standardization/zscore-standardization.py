import numpy as np

def zscore_standardize(X: np.ndarray, axis: int=0, eps: float=1e-12) -> np.ndarray:
    """
    Standardize X: (X - mean)/std. If 2D and axis=0, per column.
    Return np.ndarray (float).
    """
    # Write code here
    X = np.asarray(X, dtype=float)

    mean = np.mean(X, axis=axis, keepdims=True)

    std = np.std(X, axis=axis, keepdims=True)
    #std = np.maximum(std, eps)
    std = std + eps
    Z = (X - mean) / std


    return Z