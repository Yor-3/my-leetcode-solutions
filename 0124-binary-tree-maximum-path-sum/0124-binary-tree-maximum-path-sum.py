# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def helper(root):
            nonlocal res

            if not root:
                return 0

            maxl = helper(root.left)
            maxr = helper(root.right)

            maxl = max(maxl,0)
            maxr = max(maxr,0)

            res= max(res,root.val+maxl+maxr)
            return root.val+max(maxl,maxr)

        helper(root)

        return res