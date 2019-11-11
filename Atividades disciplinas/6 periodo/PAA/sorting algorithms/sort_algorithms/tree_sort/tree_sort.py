import numpy as np
from time import clock
from ..sort import Sort

class TreeSort(Sort):
    def __init__(self, tree_class, *args, **kwargs):
        self.tree_class = tree_class
        self.time_to_insert = None
        self.time_to_inorder_travel = None
        self.args = args
        self.kwargs = kwargs

        super().__init__()

    def _sort(self, elements, shuffle = False):
        if shuffle:
            elements = np.random.shuffle(elements)
        
        tree = self.tree_class(*self.args, **self.kwargs)

        time_insert_ini = clock()
        for element in elements:
            tree.insert(element)
        
        self.time_to_insert = clock() - time_insert_ini
        
        time_inorder_travel_ini = clock()
        orded_array = tree.in_order()
        
        self.time_to_inorder_travel = time_inorder_travel_ini - clock()

        return orded_array


    def _info(self):
        return {
            "time_to_insert" : self.time_to_insert,
            "time_to_inorder_travel" :  self.time_to_inorder_travel,
        }