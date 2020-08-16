class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        before_profit = [] 
        after_profit = [] 
        
        # find profit before each time point. price[i] serves as a selling price
        buy_price, max_profit = prices[0], 0
        for price in prices:
            buy_price = min(buy_price, price)
            max_profit = max(max_profit, price-buy_price)
            before_profit.append(max_profit)
                 
        # find profit after each time point. price[i] serves as a buying price
        sell_price, max_profit = prices[-1], 0
        for price in reversed(prices):
            sell_price = max(sell_price, price)
            max_profit = max(max_profit, sell_price-price)
            after_profit.append(max_profit)
        after_profit = list(reversed(after_profit))
        
        # find the maximum profit
        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, before_profit[i] + after_profit[i])
        return max_profit
        
