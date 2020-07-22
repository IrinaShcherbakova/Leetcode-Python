class Solution:
    import heapq
    
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        heapq.heapify(heap)
        count, num = 0, 0
        while count < n:
            num = heapq.heappop(heap)
            count += 1
            if num % 5 == 0:
                heapq.heappush(heap, num*5)
            elif num %3 == 0:
                heapq.heappush(heap, num*3)
                heapq.heappush(heap, num*5)
            else:
                heapq.heappush(heap, num*2)
                heapq.heappush(heap, num*3)
                heapq.heappush(heap, num*5)
        return num
    
    

        
        












            
        
        
