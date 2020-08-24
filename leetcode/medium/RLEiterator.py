class RLEIterator:

    def __init__(self, A: List[int]):
        self.sequence = A
        self.index = 0
    
    
    def next(self, n: int) -> int:
        while self.index < len(self.sequence)-1 and self.sequence[self.index] < n:
            n -= self.sequence[self.index]
            self.index += 2
        if self.index >= len(self.sequence)-1:
            return -1
        self.sequence[self.index] -= n
        return self.sequence[self.index+1]
        
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
