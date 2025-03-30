from bisect import bisect_left

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        res = 0
        idx = 0  # Index in cookie array

        for child in g:
            # Find the smallest valid cookie for current child
            idx = bisect_left(s, child, idx)

            # If a valid cookie exists, satisfy the child
            if idx < len(s):
                res += 1
                idx += 1  # Move to the next available cookie

        return res
