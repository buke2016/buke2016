class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Create the root node with value 1
root = TreeNode(1)

# Create the left and right child nodes of the root
left_child = TreeNode(2)
right_child = TreeNode(3)

# Set the left and right child nodes of the root
root.left = left_child
root.right = right_child

# Create the left and right child nodes of the left child
left_child_left = TreeNode(4)
left_child_right = TreeNode(5)

# Set the left and right child nodes of the left child
left_child.left = left_child_left
left_child.right = left_child_right

# Create the left and right child nodes of the right child
right_child_left = TreeNode(6)
right_child_right = TreeNode(7)

# Set the left and right child nodes of the right child
right_child.left = right_child_left
right_child.right = right_child_right