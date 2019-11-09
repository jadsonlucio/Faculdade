import pytest
from tree_sort import TreeSort
from trees.avl_tree import AVLTree
from trees.normal_tree import NormalTree


def test_normal_tree_sort():
    array = [1,3,-1,5,-4,7]
    tree_sort = TreeSort(NormalTree)
    array_sorted = tree_sort.sort(array)

    assert array_sorted == [-4, -1, 1, 3, 5, 7]

def test_avl_tree_sort():
    array = [1,3,-1,5,-4,7]
    tree_sort = TreeSort(AVLTree)
    array_sorted = tree_sort.sort(array)
    
    assert array_sorted == [-4, -1, 1, 3, 5, 7]