class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # print("gas: %s" %gas)
        # print("cost: %s" %cost)
        for i in range(len(gas)):
            if self.possibleRoute(gas, cost, i):
                return i
        return -1
    
    
    def possibleRoute(self, gas: List[int], cost: List[int], start: int) -> bool:
        # print("start index is %s" %start)
        if gas[start] < cost[start]:
            return False
        tank = gas[start] - cost[start]
        # print("tank is %s" %tank)
        i = (start+1 if start < len(gas)-1 else 0)
        while i != start:
            tank = tank + gas[i] - cost[i]
            # print("updated tank is %s" %tank)
            if tank < 0:
                return False
            i = (i+1 if i < len(gas)-1 else 0)
        return True
            
        
        
        
