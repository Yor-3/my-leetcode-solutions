from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x):
            rotate_top = rotate_bottom = 0
            for t, b in zip(tops, bottoms):
                if t != x and b != x:
                    return float('inf')  
                elif t != x:
                    rotate_top += 1
                elif b != x:
                    rotate_bottom += 1
            return min(rotate_top, rotate_bottom)

        candidate1 = tops[0]
        candidate2 = bottoms[0]

        res = min(check(candidate1), check(candidate2 if candidate1 != candidate2 else float('inf')))
        return res if res != float('inf') else -1
