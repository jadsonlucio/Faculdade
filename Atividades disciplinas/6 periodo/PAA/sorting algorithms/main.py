import numpy as np
from time import clock
from random import randint

from sort_algorithms.tree_sort.tree_sort import TreeSort
from sort_algorithms.tree_sort.trees.normal_tree import NormalTree
from sort_algorithms.tree_sort.trees.avl_tree import AVLTree


def test_sort_algorithm_time_execution(sort_obj, array, num_iterations, *args, **kwargs):
    time_executions = []

    for cont in range(num_iterations):
        tempo_inicial = clock()
        sort_obj.sort(array, *args, **kwargs)
        tempo_final = clock()

        time_executions.append([tempo_final - tempo_inicial, sort_obj.info])
    
    return time_executions

def test_synthetic_arrays(sort_obj, arrays_sizes, num_iterations, *args, **kwargs):
    time_executions = {}

    for array_size in arrays_sizes:
        array_crescent_order = [cont for cont in range(array_size)]
        array_decrescent_order = [cont for cont in range(array_size, 0, -1)]

        time_crescent_order = test_sort_algorithm_time_execution(sort_obj, array_crescent_order,
                                                            num_iterations, *args, **kwargs)
        time_decrescent_order = test_sort_algorithm_time_execution(sort_obj, array_decrescent_order,
                                                            num_iterations, *args, **kwargs)

        array_shuffle = array_crescent_order.copy()
        np.random.shuffle(array_shuffle)
        time_shuffle_order = test_sort_algorithm_time_execution(sort_obj, array_shuffle,
                                                        num_iterations, *args, **kwargs)
        
        time_executions[array_size] = {
            "time_crescent_order" : time_crescent_order,
            "time_decrescent_order" : time_decrescent_order,
            "time_shuffle_order" : time_shuffle_order
        }

    
    return time_executions


def test_tree_sort():
    tree_sort_avl = TreeSort(AVLTree)
    tree_sort_normal = TreeSort(NormalTree)
    
    time_executions_avl = test_synthetic_arrays(tree_sort_avl, [10, 100, 100], 4)
    time_executions_normal = test_synthetic_arrays(tree_sort_normal, [10, 100, 100], 4)

    return {
        "time_executions_avl" : time_executions_avl,
        "time_executions_normal" : time_executions_normal
    }


print(test_tree_sort())