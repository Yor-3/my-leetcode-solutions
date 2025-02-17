from typing import List

class Solution:
    def maxProfit(self, p: List[int]) -> int:
        if not p or len(p) < 2:
            return 0  # Edge case: no transactions possible

        b = 0  # Buy pointer
        maxp = 0  # Maximum profit

        for s in range(1, len(p)):  # Iterate over sell days
            if p[s] < p[b]:  
                b = s  # Update buying point if a lower price is found
            else:
                maxp = max(maxp, p[s] - p[b])  # Calculate profit

        return maxp
