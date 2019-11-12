import numpy as np

def mse(y_real, y_pred):
    y_real = np.array(y_real)
    y_pred = np.array(y_pred)

    return sum((y_real - y_pred)**2) / len(y_real)
