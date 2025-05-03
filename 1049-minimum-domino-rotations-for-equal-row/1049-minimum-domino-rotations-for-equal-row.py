from collections import defaultdict


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        up = defaultdict(int)
        down = defaultdict(int)

        for t, b in zip(tops, bottoms):
            up[t] += 1
            down[b] += 1

       
        combined = defaultdict(int)
        for key in set(up) | set(down):
            combined[key] = up[key] + down[key]

        needednum = -1
        n = len(tops)

        
        for key in combined:
            if combined[key] >= n:
                needednum = key
                break

        if needednum == -1:
            return -1

        
        rotate_top = 0
        rotate_bottom = 0
        for t, b in zip(tops, bottoms):
            if t != needednum and b != needednum:
                return -1  
            if t != needednum:
                rotate_top += 1
            if b != needednum:
                rotate_bottom += 1

        return min(rotate_top, rotate_bottom)
