from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        prev = [0] * n

        prev[0] = grid[0][0]

        for j in range(1, n):
            prev[j] = prev[j-1] + grid[0][j]

        for i in range(1, m):
            cur = [0] * n
            cur[0] = prev[0] + grid[i][0]
            for j in range(1, n):
                cur[j] = min(cur[j-1], prev[j]) + grid[i][j]
            prev = cur

        return prev[n-1]
