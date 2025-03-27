# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        
        if not root:
            return []

        def traverse(node, path):
            if not node:
                return
            
            # Add current node value to the path
            path.append(str(node.val))
            
            # If it's a leaf node, add the path to the result
            if not node.left and not node.right:
                res.append("->".join(path))
            
            # Traverse left and right children
            traverse(node.left, path)
            traverse(node.right, path)

            # Backtrack by removing the last node
            path.pop()

        traverse(root, [])
        
        return res
