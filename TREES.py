class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
    
    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(value, current_node.right)
        else:
            print("Value already exists in tree!")
    
    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)
    
    def _print_tree(self, current_node):
        if current_node is not None:
            self._print_tree(current_node.left)
            print(str(current_node.value))
            self._print_tree(current_node.right)


tree = BinaryTree()
tree.insert(45)
tree.insert(27)
tree.insert(67)
tree.insert(36)
tree.insert(56)
tree.insert(15)
tree.insert(75)

tree.print_tree()
