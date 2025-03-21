# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

    
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        def inorder(root):
            stack = []

            while stack or root:
                while root:
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                yield root.val
                root = root.right

        def reverse_inorder(root):
            stack = []
            while stack or root:
                while root:
                    stack.append(root)
                    root = root.right
                root = stack.pop()
                yield root.val
                root =root.left

        left_gen =inorder(root)

        right_gen = reverse_inorder(root)

        left = next(left_gen,None)  
        right = next(right_gen,None)

        while left is not None and right is not None and left<right:
            s =left+right
            if s == k:
                return True

            elif s>k:
                right = next(right_gen,None)

            else:
                left = next(left_gen,None)

        return False     