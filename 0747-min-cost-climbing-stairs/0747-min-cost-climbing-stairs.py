class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1]*len(cost)
        n = len(cost)

        dp[0] = cost[0]
        dp[1] =cost[1]

        for i in range(2,n):
            dp[i] = min(dp[i-1],dp[i-2])+cost[i]

        return min(dp[n-2],dp[n-1])