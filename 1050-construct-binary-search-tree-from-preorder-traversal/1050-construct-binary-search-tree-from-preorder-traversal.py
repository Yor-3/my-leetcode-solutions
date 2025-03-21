# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

class Solution:
    def buildBST(self, preorder: List[int], i: List[int], bound: int) -> Optional[TreeNode]:
        # Base case: check if index is out of range or current value exceeds the bound
        if i[0] == len(preorder) or preorder[i[0]] > bound:
            return None

        # Create the root node and increment the index
        root = TreeNode(preorder[i[0]])
        i[0] += 1

        # Recursively build the left and right subtrees
        root.left = self.buildBST(preorder, i, root.val)
        root.right = self.buildBST(preorder, i, bound)

        return root

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        i = [0]  # Use a mutable list to track the index across recursive calls
        return self.buildBST(preorder, i, float('inf'))
