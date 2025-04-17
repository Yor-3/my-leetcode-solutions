class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        n = len(nums)

        dp = [False] * (target + 1)
        dp[0] = True  # sum 0 is always possible

        if nums[0] <= target:
            dp[nums[0]] = True

        for i in range(1, n):
            curr = [False] * (target + 1)
            curr[0] = True  # sum 0 is always possible
            for s in range(1, target + 1):
                notpick = dp[s]
                pick = False
                if nums[i] <= s:
                    pick = dp[s - nums[i]]
                curr[s] = pick or notpick
            dp = curr

        return dp[target]
