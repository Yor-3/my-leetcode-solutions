class Solution:
    def f(self,i,j,dp):
        if i==0 and j == 0:
            dp[0][0]=1
            return 1

        if dp[i][j]!=-1:
            return dp[i][j]
        l=0
        if j-1 >-1:
            l = self.f(i,j-1,dp)
        
            
        r= 0
        if i-1>-1:
            r = self.f(i-1,j,dp)
      


        dp[i][j] =  (l+r)
        return dp[i][j]
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)]for _ in range(m)]

        return self.f(m-1,n-1,dp)
        