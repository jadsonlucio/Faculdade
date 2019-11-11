# based on https://alphafan.github.io/posts/avl_tree.html

from .tree_interface import Tree, Node

# Python code to insert a node in AVL tree
 
# Generic tree node class
# Python code to insert a node in AVL tree
 
# Generic tree node class
class AVLNode(Node):
    def __init__(self, element):
        super().__init__(element)
        self.element = element
        self.height = 1
 
# AVL tree class which supports the 
# Insert operation
class AVLTree(Tree):
    def __init__(self):
        super().__init__()

    def insert(self, element):
        if self.root_node == None:
            self.root_node = AVLNode(element)
        else:
            self.root_node = self._insert(self.root_node, element)

    # Recursive function to insert key in 
    # subtree rooted with node and returns
    # new root of subtree.
    def _insert(self, root, key):
     
        # Step 1 - Perform normal BST
        if not root:
            return AVLNode(key)
        elif key < root.element:
            root.node_left = self._insert(root.node_left, key)
        else:
            root.node_right = self._insert(root.node_right, key)
 
        # Step 2 - Update the height of the 
        # ancestor node
        root.height = 1 + max(self.getHeight(root.node_left),
                           self.getHeight(root.node_right))
 
        # Step 3 - Get the balance factor
        balance = self.getBalance(root)
 
        # Step 4 - If the node is unbalanced, 
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.node_left.element:
            return self.rightRotate(root)
 
        # Case 2 - Right Right
        if balance < -1 and key > root.node_right.element:
            return self.leftRotate(root)
 
        # Case 3 - Left Right
        if balance > 1 and key > root.node_left.element:
            root.node_left = self.leftRotate(root.node_left)
            return self.rightRotate(root)
 
        # Case 4 - Right Left
        if balance < -1 and key < root.node_right.element:
            root.node_right = self.rightRotate(root.node_right)
            return self.leftRotate(root)
 
        return root
 
    def leftRotate(self, z):
 
        y = z.node_right
        T2 = y.node_left
 
        # Perform rotation
        y.node_left = z
        z.node_right = T2
 
        # Update heights
        z.height = 1 + max(self.getHeight(z.node_left),
                         self.getHeight(z.node_right))
        y.height = 1 + max(self.getHeight(y.node_left),
                         self.getHeight(y.node_right))
 
        # Return the new root
        return y
 
    def rightRotate(self, z):
 
        y = z.node_left
        T3 = y.node_right
 
        # Perform rotation
        y.node_right = z
        z.node_left = T3
 
        # Update heights
        z.height = 1 + max(self.getHeight(z.node_left),
                        self.getHeight(z.node_right))
        y.height = 1 + max(self.getHeight(y.node_left),
                        self.getHeight(y.node_right))
 
        # Return the new root
        return y
 
    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.node_left) - self.getHeight(root.node_right)

 
 
# Driver program to test above function
myTree = AVLTree()

 
myTree.insert(10)
myTree.insert(20) 
myTree.insert(30)
myTree.insert(40)
myTree.insert(50)
myTree.insert(25)
 
"""
The constructed AVL Tree would be
            30
           /  \
         20   40
        /  \     \
       10  25    50
"""
 
# Preorder Traversal
print("Preorder traversal of the",
      "constructed AVL tree is")
print(myTree._in_order(myTree.root_node))
print()

