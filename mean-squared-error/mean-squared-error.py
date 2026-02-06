import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    y_pred = np.asarray(y_pred, dtype=float)
    y_true = np.asarray(y_true, dtype=float)
    if y_pred.shape == y_true.shape:
        return np.mean((y_true - y_pred)**2)
    else:
        return None