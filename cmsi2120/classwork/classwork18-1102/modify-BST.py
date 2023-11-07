# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root) -> list[int]:
        if not root:
            return []
        
        def inorder(node):
            nonlocal max_count, current_count, prev_value, modes
            if not node:
                return
            
            inorder(node.left)
            
            if node.val == prev_value:
                current_count += 1
            else:
                current_count = 1
            
            if current_count > max_count:
                max_count = current_count
                modes = [node.val]
            elif current_count == max_count:
                modes.append(node.val)
            
            prev_value = node.val
            
            inorder(node.right)
        
        max_count = 0
        current_count = 0
        prev_value = None
        modes = []
        
        inorder(root)
        
        return modes
