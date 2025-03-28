# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if not root.left and not root.right:
            return True

        leftval = root.left.val if root.left else 0
        rightval = root.right.val if root.right else 0

        if root.val  != leftval+rightval:
            return False

        left = self.checkTree(root.left)
        right =self.checkTree(root.right)

        return True if left and right else False