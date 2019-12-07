import numpy as np

def euclidian_distance(x, y):
    #print(x, y)
    return sum((np.array(x) - np.array(y))**2)**0.5