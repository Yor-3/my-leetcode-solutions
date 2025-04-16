from typing import List

class Solution:
    def uniquePathsWithObstacles(self, g: List[List[int]]) -> int:
        m, n = len(g), len(g[0])
        prev = [0] * n

        for i in range(m):
            cur = [0] * n
            for j in range(n):
                if g[i][j] == 1:
                    cur[j] = 0  
                elif i == 0 and j == 0:
                    cur[j] = 1  
                else:
                    up = prev[j] if i > 0 else 0
                    left = cur[j - 1] if j > 0 else 0
                    cur[j] = up + left
            prev = cur

        return prev[n - 1]
