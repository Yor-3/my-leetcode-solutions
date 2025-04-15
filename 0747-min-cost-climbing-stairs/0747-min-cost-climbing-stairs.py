class Solution:
    def f(self,n,cost,dp):
        if n == 0:
            return cost[0]

        if n==1:
            return cost[1]

        if dp[n]!=-1:
            return dp[n]

        l = self.f(n-1,cost,dp)+cost[n]
        r = self.f(n-2,cost,dp)+cost[n]
        dp[n]=min(l,r)    
        return dp[n]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1]*(len(cost))

        return min(self.f(len(cost)-1,cost,dp),self.f(len(cost)-2,cost,dp))
        