class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper function to check if a subtree is a valid BST
        def is_valid_subtree(node, lower, upper):
            if node is None:
                return True
            if not (lower < node.val < upper):
                return False
            # Check left and right subtrees
            return (is_valid_subtree(node.left, lower, node.val) and
                    is_valid_subtree(node.right, node.val, upper))
        
        # Initialize the helper function with root, negative infinity, and positive infinity
        return is_valid_subtree(root, float('-inf'), float('inf'))
