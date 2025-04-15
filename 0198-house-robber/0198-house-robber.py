class Solution:

    def f(self,n,nums,dp):
        if n==0:
            return nums[0]


        if n<0:
            return 0

        if dp[n]!=-1:
            return dp[n]
        pick = nums[n]+self.f(n-2,nums,dp)
        not_pick = self.f(n-1,nums,dp)
        dp[n] = max(pick,not_pick)

        return dp[n]


    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp = [-1]*n
        return self.f(len(nums)-1,nums,dp)

        