

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        after = [[0] * 3 for _ in range(2)]
        curr = [[0] * 3 for _ in range(2)]

        for i in range(n - 1, -1, -1):
            for bs in range(2):
                for cap in range(1, 3):
                    if bs:
                        buy = -prices[i] + after[0][cap]
                        skip = after[1][cap]
                        curr[bs][cap] = max(buy, skip)
                    else:
                        sell = prices[i] + after[1][cap - 1]
                        skip = after[0][cap]
                        curr[bs][cap] = max(sell, skip)
            after = [curr_row[:] for curr_row in curr]

        return after[1][2]
