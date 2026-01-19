class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = 0

        for i in nums:
            arr^=i
        nor = 0
        for i in range(len(nums)+1):
            nor ^=i

        return (nor^arr)