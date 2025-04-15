class Solution:

   


    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp = [-1]*n
        

        dp[0] =nums[0]
        for i in range(1,n):
            pick = nums[i]+(dp[i-2] if i>1 else 0)
            notpick = dp[i-1]

            dp[i] = max(pick,notpick)

        return dp[n-1]

        