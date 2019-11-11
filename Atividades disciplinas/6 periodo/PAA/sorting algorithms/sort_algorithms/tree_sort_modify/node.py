import numpy as np

size = 0

def binary_search(nodes, search_node):
    inf = 0
    sup = len(nodes) - 1
    meio = None

    while(inf <= sup):
        meio = (inf + sup) // 2

        if search_node.element == nodes[meio].element or  search_node.element == nodes[meio + 1].element:
            return nodes[meio]
        elif search_node.element > nodes[meio].element and search_node.element < nodes[meio + 1].element:
            return nodes[meio]
        elif search_node.element < nodes[meio].element:
            sup = meio - 1
        else:
            inf = meio + 1

class NodeTreeModify():
    def __init__(self, element):
        self.element = element
        self.left_nodes = []
        self.right_nodes = []

    
    def binary_search(self, search_node, left = True):
        if left:
            return binary_search(self.left_nodes, search_node)
        else:
            return binary_search(self.right_nodes, search_node)
            

    def insert(self, node):
        if node.element <= self.element:
            if len(self.left_nodes) == 0:
                self.left_nodes.append(node)
            else:
                min_node = self.left_nodes[0]
                max_node = self.left_nodes[-1]

                if node.element <= min_node.element:
                    self.left_nodes = [node, *self.left_nodes]
                elif node.element >= max_node.element:
                    self.right_nodes = [node, *self.right_nodes]
                else:
                    selected_node = self.binary_search(node)
                    selected_node.insert(node)
        else:
            if len(self.right_nodes) == 0:
                self.right_nodes.append(node)
            else:
                min_node = self.right_nodes[0]
                max_node = self.right_nodes[-1]

                if node.element <= min_node.element:
                    self.left_nodes = [node, *self.left_nodes]
                elif node.element >= max_node.element:
                    self.right_nodes = [node, *self.right_nodes]
                else:
                    selected_node = self.binary_search(node, False)
                    selected_node.insert(node)
    
    def in_order(self):
        global size 
        left_nodes = [node.in_order() for node in self.left_nodes]

        print(self.element)

        right_nodes = [node.in_order() for node in self.right_nodes]
        
        size = size + len(left_nodes) + len(right_nodes)


if __name__ == "__main__":
    
    #np.random.shuffle(array)
    nodes = [NodeTreeModify(cont) for cont in [6, 3, 7, 1, 2, 5, 8, 1, 2, 1, 0]]

    raiz = nodes[0]

    for i,node in enumerate(nodes[1:]):
        raiz.insert(node)

    print(raiz.in_order())
    print(size)