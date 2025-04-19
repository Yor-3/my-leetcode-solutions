class Solution(object):
    def countAtLeast(self, nums, comp, ans = 0):
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] >= comp: ans += j - i; j -= 1
            else: i += 1
        return ans

    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        return self.countAtLeast(nums, lower) - self.countAtLeast(nums, upper + 1)