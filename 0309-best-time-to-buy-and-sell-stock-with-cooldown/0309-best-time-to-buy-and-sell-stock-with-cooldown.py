class Solution:
    def maxProfit(self,prices):
        if not prices:
            return 0  # If there are no prices, we can't make any profit.
        
        # Initial states:
        buy, sell, cooldown = -prices[0], 0, 0
        
        # Iterate through the prices array
        for price in prices[1:]:
            # Transition for the buy state (either hold or buy at current price)
            new_buy = max(buy, cooldown - price)
            # Transition for the sell state (either hold or sell at current price)
            new_sell = max(sell, buy + price)
            # Transition for the cooldown state (either continue cooldown or start it from a sell)
            new_cooldown = max(cooldown, sell)
            
            # Update the states
            buy, sell, cooldown = new_buy, new_sell, new_cooldown
        
        # The result will be the maximum profit when we don't hold the stock at the end
        return sell
