class Node():
    def __init__(self, element):
        self.node_left = None
        self.node_right = None
        self.element = element

class Tree():
    def __init__(self):
        self.root_node = None

    def in_order(self):
        if self.root_node == None:
            raise Exception("Elements not inserted")

        return self._in_order(self.root_node)

    def insert(self, element):
        raise NotImplementedError("method not implemented")

    def _in_order(self, node):

        if node.node_left == None:
            arr_esq = []
        else:
            arr_esq = self._in_order(node.node_left)

        arr = arr_esq + [node.element]


        if node.node_right == None:
            arr_dir = []
        else:
            arr_dir = self._in_order(node.node_right)
        
        return arr + arr_dir
