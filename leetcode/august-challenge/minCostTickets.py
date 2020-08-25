class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        print(days)
        memo = [-1] * 366
        memo[0] = 0
        for day in days:
            memo[day] = 0
        self.recurse(days, costs, 1, memo)
        return memo[-1]
     
    
    def recurse(self, days: List[int], costs: List[int], index: int, memo: List[List[int]]) -> None:
        if index == len(memo):
            return 
        
        if memo[index] < 0:
            memo[index] = memo[index-1]
            return self.recurse(days, costs, index+1, memo)
        
        # buy one-day ticket
        one_day = memo[index-1] + costs[0]
        
        # buy seven-days ticket
        start_buy = max(0, index-7)
        seven_days = memo[start_buy] + costs[1]
        
        # buy thirty-days ticket     
        start_buy = max(0, index-30)
        thirty_days = memo[start_buy] + costs[2]
        memo[index] = min(one_day, seven_days, thirty_days)  
        return self.recurse(days, costs, index+1, memo)
    
    
    
    
    
    
    
    
    
    
    
    
