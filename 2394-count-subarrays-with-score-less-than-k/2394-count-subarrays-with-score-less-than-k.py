class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = total = left = 0
        for right, x in enumerate(nums):
            total += x
            while total * (right-left + 1) >= k:
                total -= nums[left]
                left += 1
            res += right - left + 1
        return res