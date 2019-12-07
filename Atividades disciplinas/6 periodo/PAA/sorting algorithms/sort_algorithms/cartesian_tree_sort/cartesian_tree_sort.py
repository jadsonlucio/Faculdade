from .node import Node
from .nodesPriorityQueue import NodesPriorityQueue

from ..sort import Sort

class CartesianTree(Sort):
    
    def __init__ (self):
        super().__init__()

        self.root = None
        self.last = None
            
    
    def get_root (self):
        return self.root
    
    def find_lowest_node (self, node, x):
        if (node.value < x):
            return node
        elif (node.parent != None):
            return self.find_lowest_node(node.parent, x)
        else:
            return None
    
    def add_node (self, x):
        new_node = Node()
        new_node.value = x
        
        if (self.root == None):
            self.last = new_node
            self.root = new_node
            return
        
        node_z = self.find_lowest_node(self.last, x)
        
        if (node_z == None):
            new_node.left = self.root
            self.root.parent = new_node
            self.root = new_node
        else:
            new_node.left = node_z.right
            node_z.right = new_node
            new_node.parent = node_z
            
        self.last = new_node
        
    def in_order_traversal(self, node):
        if (node == None):
            return
        self.in_order_traversal(node.left)
        print(node.value)
        self.in_order_traversal(node.right)
        
    #FUNÇÃO QUE REALIZA O SORTING
        
    def cartesian_tree_sort (self, sorted_ar):
        p_queue = NodesPriorityQueue()
        p_queue.push(self.root)
        temp = None
            
        while not(p_queue.isEmpty()):
            temp = p_queue.smallest()
            
            #print("Começo do código, maior valor da PriorityQueue, no caso, a raiz da árvore:")
            #print(p_queue.smallest().value)
            
            p_queue.pop() 
            #print("Priority Queue depois do pop: "+ p_queue.toString())
            sorted_ar.append(temp.value)
            #print("lista ordenada até o momento: " + str(sorted_ar))
            if (temp.left != None):
                p_queue.push(temp.left)
                #print(temp.left.value)
                #p_queue.push(temp.left)
            if(temp.right != None):
                #print(temp.right.value)
                p_queue.push(temp.right)

    def _sort(self, elements):
        self.root = None
        self.last = None

        for ele in elements:
            self.add_node(ele)

        aux = []
        self.cartesian_tree_sort(aux)

        return aux
