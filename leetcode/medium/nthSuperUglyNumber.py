class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 1:
            return 1
        heaps = []
        seen = set()
        for prime in primes:
            heap = []
            heappush(heap, prime)
            heaps.append(heap)
            seen.add(prime)
        num = 0
        for i in range(n-1):
            heap_index = self.get_min(heaps)
            heap = heaps[heap_index]
            num = heappop(heap)
            for i in range(heap_index, len(primes)):
                new_prime = num * primes[i]
                if new_prime not in seen:
                    heappush(heap, num * primes[i])
                    seen.add(new_prime)
        return num
                       
            
    def get_min(self, heaps: List[List[int]]) -> int:
        heap_index, min_num = 0, heaps[0][0]
        for i, heap in enumerate(heaps):
            if heap[0] < min_num:
                min_num = heap[0]
                heap_index = i
        return heap_index
