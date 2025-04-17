class Solution:
    def minimumTotal(self, t: List[List[int]]) -> int:
        n = len(t)
        dp = [0] * n
        
        for i in range(n-1, -1, -1):
            for j in range(i+1):
                if i == n-1:
                    dp[j] = t[i][j]
                else:
                    dp[j] = t[i][j] + min(dp[j], dp[j+1])
        
        return dp[0]
