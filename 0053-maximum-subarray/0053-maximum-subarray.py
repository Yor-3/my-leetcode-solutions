class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = 0
        maxsum = float('-inf')
        n = len(nums)
        for i in range(n):
            cursum += nums[i]
            maxsum = max(cursum,maxsum)
            if cursum <0:
                cursum=0

        return maxsum