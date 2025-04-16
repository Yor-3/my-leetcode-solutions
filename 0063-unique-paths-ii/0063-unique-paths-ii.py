from typing import List

class Solution:
    def uniquePathsWithObstacles(self, g: List[List[int]]) -> int:
        m, n = len(g), len(g[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if g[i][j] == 1:
                    dp[i][j] = 0  
                elif i == 0 and j == 0:
                    dp[i][j] = 1  
                else:
                    up = dp[i - 1][j] if i > 0 else 0
                    left = dp[i][j - 1] if j > 0 else 0
                    dp[i][j] = up + left

        return dp[m - 1][n - 1]
