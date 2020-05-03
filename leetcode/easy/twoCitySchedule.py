def sortDif(nums: List[int]):
        return abs(nums[0] - nums[1])

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        result = 0
        costs.sort(reverse = True, key = sortDif)
        A = B = 0
        half = len(costs) // 2
        for cost in costs:
            if cost[0] <= cost[1] and A < half:
                result += cost[0]
                A += 1
            elif cost[0] <= cost[1] and A == half:
                result += cost[1]
                B += 1
            elif cost[1] < cost[0] and B < half:
                result += cost[1]
                B += 1
            else:
                result += cost[0]
                A += 1
        return result
        
        
    
