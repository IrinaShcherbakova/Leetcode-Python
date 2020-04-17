class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed):
            if n == 0:
                return True
            if flowerbed[i] == 0:
                if i+1 == len(flowerbed) or flowerbed[i+1] == 0:
                    n -= 1
                else:
                    i += 1
            i += 2
        return n == 0
                
                    
            
