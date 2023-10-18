class Solution:
    
    # Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        # Helper function to perform an inorder traversal and check if it's a BST.
        def isBSTUtil(node, prev):
            if node is None:
                return True
            
            # Recursively check the left subtree
            if not isBSTUtil(node.left, prev):
                return False
            
            # Check if the current node's value is greater than the previous node
            if node.data <= prev[0]:
                return False
            
            # Update the previous value
            prev[0] = node.data
            
            # Recursively check the right subtree
            return isBSTUtil(node.right, prev)
        
        # Initialize the previous value as negative infinity
        prev = [-float("inf")]
        return isBSTUtil(root, prev)
