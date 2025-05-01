class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
            
        from collections import defaultdict

        counts = defaultdict(int)
        first_index = {}
        last_index = {}

        for i, num in enumerate(nums):
            counts[num] += 1
            if num not in first_index:
                first_index[num] = i
            last_index[num] = i

        degree = max(counts.values())
        min_len = float('inf')

        for num in counts:
            if counts[num] == degree:
                length = last_index[num] - first_index[num] + 1
                min_len = min(min_len, length)

        return min_len
