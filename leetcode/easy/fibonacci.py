class Solution:
    def fib(self, N: int) -> int:
        prev = []
        prev.append(0)
        prev.append(1)
        for i in range(2, N+1):
            prev.append(prev[i-1] + prev[i-2])
        return prev[N]
