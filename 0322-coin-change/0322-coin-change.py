class Solution:
    def f(self, i, a, c,dp):
        if i == 0:
            if a % c[0] == 0:
                return a // c[0]
            else:
                return float('inf')

        if dp[i][a]!=-1:
            return dp[i][a]
        notpick = self.f(i - 1, a, c,dp)
        pick = float('inf')
        if a >= c[i]:
            pick = 1 + self.f(i, a - c[i], c,dp)


        dp[i][a]= min(pick, notpick)
        return dp[i][a]

    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)

        dp = [[-1 for _ in range(amount+1)]for _ in range(n)]
        ans = self.f(len(coins) - 1, amount, coins,dp)
        return -1 if ans == float('inf') else ans
