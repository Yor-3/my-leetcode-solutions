class Solution:
    def maxProfit(self, p: List[int]) -> int:
        profit = 0

        for i in range(1,len(p)):
            if p[i]>p[i-1]:
                profit +=p[i]-p[i-1]

        return profit