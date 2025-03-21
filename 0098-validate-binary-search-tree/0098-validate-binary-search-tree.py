# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, l, h):
            if not root:
                return True 
            
            if root.val <= l or root.val >= h:
                return False
            
            return helper(root.left, l, root.val) and helper(root.right, root.val, h)
        
        return helper(root, float('-inf'), float('inf'))
