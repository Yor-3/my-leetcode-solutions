class Solution:
    def f(self,i,j,t,dp):
        n = len(t)
        if i==n-1:
            dp[i][j] =t[i][j]
            return t[i][j]

        if j>i:
            return float('inf')

        if dp[i][j]!=-1:
            return dp[i][j]

        same = t[i][j]+self.f(i+1,j,t,dp)
        plus = t[i][j]+self.f(i+1,j+1,t,dp)

        dp[i][j]= min(same,plus)
        return dp[i][j]

    def minimumTotal(self, t: List[List[int]]) -> int:
        n = len(t)
        dp = [[-1] *(i+1) for i in range(n)]

        return self.f(0,0,t,dp)
        