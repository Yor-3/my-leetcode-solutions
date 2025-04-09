class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = set()

        for i in nums:
            if i<k:
                return -1
            elif i>k:
                seen.add(i)

        return len(seen)
