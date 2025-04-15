class Solution:
    def f(self,n,dp):
        if n==0:
            
            return 1

        if n<0:
            return 0
        if dp[n]!=-1:
            return dp[n]

        l = self.f(n-1,dp)
        r = self.f(n-2,dp)
        dp[n] = l+r
        return dp[n]
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        return self.f(n,dp)
        