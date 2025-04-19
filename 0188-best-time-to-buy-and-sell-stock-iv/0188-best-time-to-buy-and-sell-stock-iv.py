import heapq
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        def maxInc(s, e, d):
            max_inc = 0
            rs = re = s
            m = prices[s]
            mi = s
            for i in range(s + 1, e + 1):
                p = prices[i]
                inc = d * (p - m)
                if max_inc < inc:
                    rs, re, max_inc = mi, i, inc  
                elif inc < 0:
                    m, mi = p, i
            return max_inc, rs, re

        max_trade = 0
        inc, s, e = maxInc(0, len(prices) - 1, 1)
        item = (-inc, 0, s, e, len(prices) - 1, 1)
        q = [item]
        while k and q:
            minc, s, ss, ee, e, d = heapq.heappop(q)
            k -= 1
            max_trade -= minc
            new_intervals = []
            if s < ss - 1:
                new_intervals.append((s, ss - 1, d))
            if ss + 2 < ee:
                new_intervals.append((ss + 1, ee - 1, -d))
            if ee + 1 < e:
                new_intervals.append((ee + 1, e, d))
            for s, e, d in new_intervals:
                inc, ss, ee = maxInc(s, e, d)
                if 0 < inc:
                    heapq.heappush(q, (-inc, s, ss, ee, e, d))
        return max_trade



