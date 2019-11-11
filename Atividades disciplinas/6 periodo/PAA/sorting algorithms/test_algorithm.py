import sys
import numpy as np
from random import randint
from results import Results

#sys.setrecursionlimit(10000000)

def update_with_list(dict_1, dict_2):
    for key, value in dict_2.items():
        if key not in dict_1:
            dict_1[key] = [value]
        else:
            dict_1[key].append(value)
    

def test_sort_algorithm_time_execution(sort_obj, array, num_iterations, *args, **kwargs):
    info_executions = {}

    for cont in range(num_iterations):
        sort_obj.sort(array, *args, **kwargs)
        update_with_list(info_executions, sort_obj.info)

    return info_executions

def test_synthetic_arrays(sort_obj, arrays_sizes, num_iterations, *args, **kwargs):
    info_executions = {}

    for array_size in arrays_sizes:
        print(array_size)
        array_crescent_order = [cont for cont in range(array_size)]
        array_decrescent_order = [cont for cont in range(array_size, 0, -1)]

        info_crescent_order = test_sort_algorithm_time_execution(sort_obj, array_crescent_order,
                                                            num_iterations, *args, **kwargs)
        info_decrescent_order = test_sort_algorithm_time_execution(sort_obj, array_decrescent_order,
                                                            num_iterations, *args, **kwargs)

        array_shuffle = array_crescent_order.copy()
        np.random.shuffle(array_shuffle)
        info_shuffle_order = test_sort_algorithm_time_execution(sort_obj, array_shuffle,
                                                        num_iterations, *args, **kwargs)
        
        info_executions[array_size] = {
            "info_crescent_order" : info_crescent_order,
            "info_decrescent_order" : info_decrescent_order,
            "info_shuffle_order" : info_shuffle_order
        }

    return info_executions

def test_sort_algorithms_with_synthetic_data(sort_objs_dict, arrays_sizes, number_iterations = 1):
    results_dict = {}

    for sort_obj_name, sort_obj in sort_objs_dict.items():
        print(sort_obj_name)
        results_dict[sort_obj_name] = test_synthetic_arrays(sort_obj, arrays_sizes, number_iterations)

    return Results(results_dict)