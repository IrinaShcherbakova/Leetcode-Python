class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices % 2 != 0:
            return []
        if tomatoSlices == 0 and cheeseSlices == 0:
            return [0,0]
        if tomatoSlices <= 0 or cheeseSlices <= 0:
            return []       
        if tomatoSlices <= cheeseSlices:
            return []
        
        small = (4 * cheeseSlices - tomatoSlices) // 2
        jumbo = cheeseSlices - small
        if small < 0 or jumbo < 0:
            return []
        return [jumbo, small]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        
