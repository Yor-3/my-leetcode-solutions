class Solution:
    def numTilings(self,n: int) -> int:
        MOD = 10**9 + 7
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        dp = [0] * (n + 1)
        dp_partial = [0] * (n + 1)
        
        dp[0], dp[1], dp[2] = 1, 1, 2
        dp_partial[1], dp_partial[2] = 0, 1
        
        for i in range(3, n + 1):
            dp[i] = (dp[i-1] + dp[i-2] + 2 * dp_partial[i-1]) % MOD
            dp_partial[i] = (dp_partial[i-1] + dp[i-2]) % MOD
        
        return dp[n]