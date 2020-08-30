class UnionFind:
    
    def __init__(self, N: int):
        self.id = []
        self.size = []
        for i in range(N):
            self.id.append(i)
            self.size.append(1)
            
    def root(self, i: int) -> int:
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i
    
    def union(self, p: int, q: int) -> None:
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        if self.size[i] < self.size[j]:
            self.id[i] = j
            self.size[j] += self.size[i]
        else:
            self.id[j] = i
            self.size[i] += self.size[j]
            
    def max_size(self) -> int:
        return max(self.size)
        

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        uf = UnionFind(len(A))
        prime_index = {}
        for i, num in enumerate(A):
            num_primes = self.prime_factors(num)
            for prime in num_primes:
                if prime in prime_index:
                    uf.union(i, prime_index[prime])
                prime_index[prime] = i
        return uf.max_size()
        
    
    def prime_factors(self, n: int) -> set:
        primes = set()
        while n % 2 == 0:
            primes.add(2)
            n //= 2
        i = 3
        while i <= math.sqrt(n):
            while n % i == 0:
                primes.add(i)
                n //= i
            i += 2
        if n > 2:
            primes.add(n)
        return primes
        
        
        
        
        
        
