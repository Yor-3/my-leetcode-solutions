from typing import List

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        table = {}
        for num in arr:
            table[num] = table.get(num - difference, 0) + 1
        return max(table.values())