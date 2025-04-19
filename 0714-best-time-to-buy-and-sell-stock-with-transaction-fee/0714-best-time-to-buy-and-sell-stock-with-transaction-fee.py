class Solution:
    def maxProfit(self,prices, fee):

        n = len(prices)
        if n == 0:
            return 0

        
        buy = -prices[0] - fee 
        sell = 0  

        for i in range(1, n):
            
            new_buy = max(buy, sell - prices[i] - fee) 
            new_sell = max(sell, buy + prices[i])  
            
            
            buy, sell = new_buy, new_sell

        return sell  