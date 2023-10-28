# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root):
        # Initialize an empty stack to hold the nodes in the path
        self.stack = []
        # Start at the root and traverse left to the leftmost node
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        # Pop the top node from the stack, which will be the next smallest node
        node = self.stack.pop()
        # If the popped node has a right subtree, add its leftmost nodes to the stack
        if node.right:
            root = node.right
            while root:
                self.stack.append(root)
                root = root.left
        # Return the value of the popped node
        return node.val

    def hasNext(self) -> bool:
        # If the stack is not empty, there are more nodes to visit
        return len(self.stack) > 0
