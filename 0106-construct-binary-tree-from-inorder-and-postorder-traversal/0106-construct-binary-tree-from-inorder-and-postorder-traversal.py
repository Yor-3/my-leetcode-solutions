# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        inMap = {val: idx for idx, val in enumerate(inorder)}

        return self._buildTree(postorder, 0, len(postorder) - 1, inorder, 0, len(inorder) - 1, inMap)

    def _buildTree(self, postorder, postStart, postEnd, inorder, inStart, inEnd, inMap):
        if postStart > postEnd or inStart > inEnd:
            return None


        root_val = postorder[postEnd]
        root = TreeNode(root_val)

        inRoot = inMap[root_val]
        numsLeft = inRoot - inStart

        root.left = self._buildTree(postorder, postStart, postStart + numsLeft - 1,
                                    inorder, inStart, inRoot - 1, inMap)
        root.right = self._buildTree(postorder, postStart + numsLeft, postEnd - 1,
                                     inorder, inRoot + 1, inEnd, inMap)

        return root