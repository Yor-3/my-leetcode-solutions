class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        offset = total
        n = len(nums)

        if abs(target) > total:
            return 0  # target out of possible bounds

        dp = [0] * (2 * total + 1)
        dp[offset] = 1  # 1 way to make sum 0 with 0 elements

        for num in nums:
            next_dp = [0] * (2 * total + 1)
            for s in range(-total, total + 1):
                if dp[s + offset] > 0:
                    next_dp[s + num + offset] += dp[s + offset]
                    next_dp[s - num + offset] += dp[s + offset]
            dp = next_dp

        return dp[target + offset]
