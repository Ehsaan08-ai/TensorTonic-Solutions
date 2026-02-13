import numpy as np

def minmax_scale(X: np.ndarray, axis: int=0, eps: float=1e-12) -> np.ndarray:
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    X = np.asarray(X, dtype=float)

    min_x = np.min(X, axis=axis, keepdims=True)
    max_x = np.max(X, axis=axis, keepdims=True)
    denominator = max_x - min_x
    denominator = np.maximum(denominator, eps)


    X_scaled = (X - min_x) / denominator
    
    return X_scaled