class Solution:
    def minInsertions(self, s: str) -> int:
        t1=s
        t2=s[::-1]
        m, n = len(t1), len(t2)
        
        dp = ['' for _ in range(n + 1)]
        
        for i in range(1, m + 1):
            cur = ['' for _ in range(n + 1)]
            for j in range(1, n + 1):
                if t1[i - 1] == t2[j - 1]:
                    cur[j] = dp[j - 1] + t1[i - 1]
                else:
                    cur[j] = dp[j] if len(dp[j]) > len(cur[j - 1]) else cur[j - 1]
            dp = cur
        
        i = len(dp[n])
        j = len(s)

        return j-i
