class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        m, n = len(t1), len(t2)
        

        dp = [0 for _ in range(n + 1)]
        
        for i in range(1, m + 1):
            cur = [0 for _ in range(n + 1)]
            for j in range(1, n + 1):
                if t1[i - 1] == t2[j - 1]:
                    cur[j] = 1 + dp[j - 1]
                else:
                    cur[j] = max(dp[j], cur[j - 1])

            dp = cur
        
        return dp[n]
