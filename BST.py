class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        # You can add more elements such as height here if needed

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert(self, value):
        self._insert_helper(self.root, value)

    def _insert_helper(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_helper(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_helper(current_node.right, value)
        else:
            # value already exists in tree
            pass


tree = BinaryTree(5)
tree.insert(3)
tree.insert(8)
tree.insert(2)
tree.insert(4)

print(tree)
