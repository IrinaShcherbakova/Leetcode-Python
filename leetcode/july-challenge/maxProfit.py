BUY = 0
SELL = 1
COOLDOWN = 2

class Solution:    
    def maxProfit(self, prices: List[int]) -> int:
        global BUY
        memo = []
        for i in range(len(prices)):
            memo.append([-1]*3)
          
        return self.maxProfitAtDay(prices, 0, BUY, memo)
    
    
    def maxProfitAtDay(self, prices: List[int], day: int, action: int, memo: List[int]) -> int:
        global BUY, SELL, COOLDOWN
        if day >= len(prices):
            return 0
        if memo[day][action] > 0:
            return memo[day][action]
        if action == BUY:
            buy = self.maxProfitAtDay(prices, day+1, SELL, memo) - prices[day]
            dontbuy = self.maxProfitAtDay(prices, day+1, BUY, memo)
            memo[day][action] = max(buy, dontbuy)
            return memo[day][action]
        
        if action == SELL:
            sell = self.maxProfitAtDay(prices, day+1, COOLDOWN, memo) + prices[day]
            dontsell = self.maxProfitAtDay(prices, day+1, SELL, memo)
            memo[day][action] = max(sell, dontsell)
            return memo[day][action]
        
        cooldown = self.maxProfitAtDay(prices, day+1, BUY, memo) 
        memo[day][action] = cooldown
        return memo[day][action]
        
        
        
    
            
