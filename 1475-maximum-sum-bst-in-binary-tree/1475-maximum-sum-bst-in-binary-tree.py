# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res = 0
        def helper(root):
            nonlocal res
            if not root:
                return 0,float('inf'),float('-inf')

            ls,lmin,lmax = helper(root.left)
            rs,rmin,rmax = helper(root.right)

            if lmax<root.val<rmin:
                cursum = root.val +ls+rs
                res = max(res,cursum)
                return cursum,min(lmin,root.val),max(rmax,root.val)
            else:
                return max(ls,rs),float('-inf'),float('inf')
        helper(root)
        return res

            
                
        