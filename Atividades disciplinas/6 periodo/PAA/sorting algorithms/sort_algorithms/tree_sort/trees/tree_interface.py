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
        # Set current to root of binary tree 
        elements = []
        current = node  
        stack = [] # initialize stack 
        done = 0 
        
        while True: 
            
            # Reach the left most Node of the current Node 
            if current is not None: 
                
                # Place pointer to a tree node on the stack  
                # before traversing the node's left subtree 
                stack.append(current) 
            
                current = current.node_left  
    
            
            # BackTrack from the empty subtree and visit the Node 
            # at the top of the stack; however, if the stack is  
            # empty you are done 
            elif(stack): 
                current = stack.pop() 
                elements.append(current.element) # Python 3 printing 
            
                # We have visited the node and its left  
                # subtree. Now, it's right subtree's turn 
                current = current.node_right  
    
            else: 
                break

        return elements
