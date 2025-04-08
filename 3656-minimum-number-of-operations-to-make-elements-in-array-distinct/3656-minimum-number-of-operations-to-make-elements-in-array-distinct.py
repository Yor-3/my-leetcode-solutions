class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        for i, num in reversed(list(enumerate(nums))):
            if num in seen:
                return (i+3)//3

            seen.add(num)

        return 0