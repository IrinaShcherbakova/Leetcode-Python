class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        self.inc = []
        

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            
            
    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        index = len(self.stack)
        val = self.stack.pop()
        # print(self.inc)
        for pair in self.inc:
            if pair[0] >= index:  #return value lies in k bounds
                val += pair[1]    #increment return value
                pair[0] -= 1
                if pair[0] == 0:
                    pair[1] = 0
        if len(self.stack) == 0:
            self.inc = []
        return val
        
        
    def increment(self, k: int, val: int) -> None:
        if k <= len(self.stack):
            self.inc.append([k,val])
        if k > len(self.stack) and len(self.stack) > 0:
            self.inc.append([len(self.stack),val])

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
