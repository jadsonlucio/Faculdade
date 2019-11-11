from test_algorithm import test_sort_algorithms_with_synthetic_data

from sort_algorithms.bubble_sort.bubble_sort import BubbleSort
from sort_algorithms.heap_sort.heap_sort import HeapSort
from sort_algorithms.tree_sort.tree_sort import TreeSort
from sort_algorithms.tree_sort.trees.normal_tree import NormalTree
from sort_algorithms.tree_sort.trees.avl_tree import AVLTree


if __name__ == "__main__":
    tree_sort_normal = TreeSort(NormalTree, mode = "iterative")
    tree_sort_avl = TreeSort(AVLTree)
    bubble_sort = BubbleSort()
    heap_sort = HeapSort()

    dict_sort_algorithms = {
        "tree sort avl" : tree_sort_avl, 
        "bubble sort" : bubble_sort,
        "heap sort" : heap_sort
    }

    results = test_sort_algorithms_with_synthetic_data(dict_sort_algorithms, [10, 100, 250, 500, 750, 1000, 1500, 2000], 1)
    results.plot_attribute(["bubble sort", "heap sort"], "Número de escritas")