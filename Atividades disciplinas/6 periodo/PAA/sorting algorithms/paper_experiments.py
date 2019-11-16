import numpy as np

from results import Results
from test_algorithm import test_sort_algorithms_with_synthetic_data, test_sort_algorithms

from sort_algorithms.bubble_sort.bubble_sort import BubbleSort
from sort_algorithms.heap_sort.heap_sort import HeapSort
from sort_algorithms.tree_sort.tree_sort import TreeSort
from sort_algorithms.tree_sort.trees.normal_tree import NormalTree
from sort_algorithms.tree_sort.trees.avl_tree import AVLTree
from sort_algorithms.insertion_sort.insertion_sort import InsertionSort
from sort_algorithms.quick_sort.quick_sort import QuickSort
from sort_algorithms.merge_sort.merge_sort import MergeSort
from sort_algorithms.selection_sort.selection_sort import SelectionSort

tree_sort_normal = TreeSort(NormalTree, mode = "iterative")
tree_sort_avl = TreeSort(AVLTree)
bubble_sort = BubbleSort()
heap_sort = HeapSort()
insertion_sort = InsertionSort()
quick_sort = QuickSort()
merge_sort = MergeSort()
selection_sort = SelectionSort()

dict_sort_algorithms = {
    "tree sort normal" : tree_sort_normal,
    "tree sort avl" : tree_sort_avl, 
    "bubble sort" : bubble_sort,
    "heap sort" : heap_sort,
    "insertion sort" : insertion_sort,
    "quick sort" : quick_sort,
    "merge sort" : merge_sort,
    "selection sort" : selection_sort
}

def shuffle_array(array, num_shuffles):
    for c in range(num_shuffles):
        index_1 = np.random.randint(len(array))
        index_2 = np.random.randint(len(array))

        array[[index_1, index_2]] = array[[index_2, index_1]]
    
    return array

def test_sort_algorithms_with_synthetic_arrays(selected_algorithms = None, array_sizes = None, 
                    num_iterations = 1, file_name = "synthetic_arrays_test.json", reset = True):

    if selected_algorithms == None and array_sizes == None and not reset:
        results = Results.load_results(file_name)
    else:
        dict_algorithms = {selected_algorithm : dict_sort_algorithms[selected_algorithm] 
                                            for selected_algorithm in selected_algorithms}
        results = test_sort_algorithms_with_synthetic_data(dict_algorithms, array_sizes, num_iterations)
        results = Results(results, ["Nome do algoritmo", "Tamanho entrada", "Tipo array", "atributo", "Valor"])
        results.save(file_name)

    return results

def test_sort_algorithms_with_shuffle_arrays(selected_algorithms = None, array_size = None, 
                                            shuffle_percentages = None, num_iterations = 1, 
                                            file_name = "shuffle_arrays.json", reset = True):
    
    if selected_algorithms == None and array_size == None and not reset:
        results = Results.load_results(file_name)
    else:
        dict_algorithms = {selected_algorithm : dict_sort_algorithms[selected_algorithm] 
                                            for selected_algorithm in selected_algorithms}
        
        arrays_dict = {}

        for shuffle_percentage in shuffle_percentages:
            number_shuffles = int(array_size * shuffle_percentage)
            array = np.array(list(range(array_size)))
            arrays_dict[shuffle_percentage] = shuffle_array(array, number_shuffles)

        results = test_sort_algorithms(dict_algorithms, arrays_dict)
        results = Results(results, ["Nome do algoritmo", "Porcentagem de desordenação", "atributo", "Valor"])
        results.save(file_name)
    

    return results