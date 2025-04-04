# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return (None,0)

            left,lheight = dfs(node.left)
            right,rheight =dfs(node.right)

            if lheight == rheight:
                return node, rheight+1
            elif lheight>rheight:
                return left,lheight+1
            else:
                return right,rheight+1

        res,_ = dfs(root)

        return res

            
        