from .tree_interface import Tree, Node

class NormalNode(Node):
    def __init__(self, element):
        super().__init__(element)

class NormalTree(Tree):
    def __init__(self, mode = "recursive"):
        self.mode = mode
        super().__init__()

    def insert(self, element):
        if self.root_node == None:
            self.root_node = NormalNode(element)
        else:
            self._insert(self. root_node, element)

    def _insert(self, current_node, element):
        if self.mode == "recursive":
            self._insert_with_recursion(current_node, element)
        elif self.mode == "iterative":
            self._insert_with_iteration(current_node, element)

    def _insert_with_recursion(self, current_node, element):
        if current_node.element < element:
            if current_node.node_right == None:
                current_node.node_right = NormalNode(element)
            else:
                self._insert(current_node.node_right, element)
        else:
            if current_node.node_left == None:
                current_node.node_left = NormalNode(element)
            else:
                self._insert(current_node.node_left, element)
    

    def _insert_with_iteration(self, current_node, element):
        while(True):
            if current_node.element < element:
                if current_node.node_right == None:
                    current_node.node_right = NormalNode(element)
                    break
                else:
                    current_node = current_node.node_right
            else:
                if current_node.node_left == None:
                    current_node.node_left = NormalNode(element)
                    break
                else:
                    current_node = current_node.node_left
