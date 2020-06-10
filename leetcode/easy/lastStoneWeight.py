class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        temp = []
        while len(stones) > 1:
            newStone = stones.pop() - stones.pop()
            if newStone > 0:
                stones.append(newStone)
                stones.sort()
        return (0 if len(stones) == 0 else stones[0])
            
