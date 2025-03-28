# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, a: List[int], b: List[int]) -> Optional[TreeNode]:
        
        if not a or not b:
            return None

        root = TreeNode(b.pop())

        ind= a.index(root.val)
        root.right = self.buildTree(a[ind+1:],b)
        root.left = self.buildTree(a[:ind],b)

        return root