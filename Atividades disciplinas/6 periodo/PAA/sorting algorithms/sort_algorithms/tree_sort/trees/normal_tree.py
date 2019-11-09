from .tree_interface import Tree, Node

class NormalNode(Node):
    def __init__(self, element):
        super().__init__(element)

class NormalTree(Tree):
    def __init__(self):
        self.root_node = None

    def insert(self, element):
        if self.root_node == None:
            self.root_node = NormalNode(element)
        else:
            self._insert(self. root_node, element)

    def _insert(self, current_node, element):
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
    

    
