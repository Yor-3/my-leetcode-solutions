class Solution:
    def f(self,i1,i2,t1,t2,dp):
        if i1<0 or i2<0:
            return 0

        if dp[i1][i2]!=-1:
            return dp[i1][i2]
        
        if t1[i1]==t2[i2]: 
            dp[i1][i2] = 1+self.f(i1-1,i2-1,t1,t2,dp)
            return dp[i1][i2]

        else:
            dp[i1][i2] = max(self.f(i1-1,i2,t1,t2,dp),self.f(i1,i2-1,t1,t2,dp))
            return dp[i1][i2]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n = len(text2)

        dp = [[-1 for _ in range(n)]for _ in range(m) ]



        return self.f(m-1,n-1,text1,text2,dp)