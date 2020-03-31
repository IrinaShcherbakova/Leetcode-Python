class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True]*(n)
        i = 2
        while i*i < n:
            if not primes[i]:
                i += 1
                continue
            j = i * i
            while j < n:
                #print("set %s to false" % j)
                primes[j] = False
                j += i
            i += 1
        count = 0
        #print("")
        for i in range(2, n):
            if primes[i]:
                #print(i)
                count += 1
        return count
