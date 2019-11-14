import numpy as np
from ..sort import Sort

class BogoSort(Sort):
    def __init__(self):
        super().__init__()

    
    def is_sorted(self, array):
        return np.all([array[c] > array[c+1] for c in range(len(array) - 1)])

    def sort(self, elements):
        while(True):
            np.random.shuffle(elements)
            if self.is_sorted(elements):
                return elements
            