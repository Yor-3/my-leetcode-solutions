from collections import defaultdict
from math import gcd
from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        index_map = defaultdict(list)
        for idx, val in enumerate(nums):
            index_map[val].append(idx)
        
        ans = 0
        for indices in index_map.values():
            freq = defaultdict(int)
            for i in indices:
                g = gcd(i, k)
                for d in freq:
                    if (g * d) % k == 0:
                        ans += freq[d]
                freq[g] += 1
        return ans
