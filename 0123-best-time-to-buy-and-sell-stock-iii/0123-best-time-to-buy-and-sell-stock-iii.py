class Solution:
    def f(self,i,bs,cap,p,dp):

        if i==len(p) or cap == 0:
            return 0

        if dp[i][bs][cap]!=-1:
            return dp[i][bs][cap]
        if bs:
            
            dp[i][bs][cap]=max(-p[i]+self.f(i+1,0,cap,p,dp),self.f(i+1,1,cap,p,dp))
            return dp[i][bs][cap]
        else:
            dp[i][bs][cap]=max(p[i]+self.f(i+1,1,cap-1,p,dp),self.f(i+1,0,cap,p,dp))
            return dp[i][bs][cap]

        
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[[-1 for i in range(3)]for i in range(2)] for i in range(len(prices))]
        return self.f(0,1,2,prices,dp)
        