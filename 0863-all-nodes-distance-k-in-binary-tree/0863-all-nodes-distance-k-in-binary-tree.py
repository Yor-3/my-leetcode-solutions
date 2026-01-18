# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        parent = {}
        q = deque()
        q.append(root)

        while q:
            size = len(q)
            for _ in range(size):
                top = q.popleft()

                if top.left:
                    q.append(top.left)
                    parent[top.left.val] = top


                if top.right:
                    q.append(top.right)
                    parent[top.right.val] = top



        visited = {}
        q.append(target)

        while k>0 and q:
            size = len(q)

            for _ in range(size):
                top = q.popleft()
                visited[top.val] = 1
                if top.left and top.left.val not in visited:
                    q.append(top.left)

                if top.right and top.right.val not in visited:
                    q.append(top.right)

                if top.val in parent and parent[top.val].val not in visited:
                    q.append(parent[top.val])

            k-=1

        while q:
            ans.append(q.popleft().val)
        return ans