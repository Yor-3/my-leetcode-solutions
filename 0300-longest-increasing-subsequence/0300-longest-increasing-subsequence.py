class Solution:
    # def f(self, i, p, nums, dp):
    #     n = len(nums)
    #     if i == n:
    #         return 0

    #     if dp[i][p + 1] != -1:
    #         return dp[i][p + 1]

    #     size = self.f(i + 1, p, nums, dp)
    #     if p == -1 or nums[p] < nums[i]:
    #         size = max(size, 1 + self.f(i + 1, i, nums, dp))

    #     dp[i][p + 1] = size
    #     return size

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # dp = [[0 for _ in range(n + 1)] for _ in range(n+1)]
        # for i in range(n-1,-1,-1):
        #     for p in range(i-1,-2,-1):
        #         size = dp[i+1][p+1]

        #         if p ==-1 or nums[p]<nums[i]:

        #             size = max(size,1+dp[i+1][i+1])

        #         dp[i][p+1]=size

        # return dp[0][0]
        dp = [0 for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            prev = [0 for _ in range(n+1)]
            for p in range(i-1,-2,-1):
                size = dp[p+1]
                if p==-1 or nums[p]<nums[i]:
                    size = max(size,1+dp[i+1])
                prev[p+1] = size

            dp = prev

        return dp[0]



        
