class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

def RemoveTreeNode(tree, node):
    if tree.root is None or node is None:
        return

    if node.left is None and node.right is None:
        # Case A: Deleting a leaf node.
        if node.parent is None:
            tree.root = None
        elif node.parent.left == node:
            node.parent.left = None
        else:
            node.parent.right = None
    elif node.left is None or node.right is None:
        # Case B: Deleting a node with one child.
        if node.left is None:
            child = node.right
        else:
            child = node.left
        child.parent = node.parent
        if node.parent is None:
            tree.root = child
        elif node.parent.left == node:
            node.parent.left = child
        else:
            node.parent.right = child
    else:
        # Case C: Deleting a node with two children.
        successor = node.right
        while successor.left is not None:
            successor = successor.left

        RemoveTreeNode(tree, successor)

        if node.parent is None:
            tree.root = successor
        elif node.parent.left == node:
            node.parent.left = successor
        else:
            node.parent.right = successor

        successor.parent = node.parent
        successor.left = node.left
        if node.left is not None:
            node.left.parent = successor
        successor.right = node.right
        if node.right is not None:
            node.right.parent = successor
