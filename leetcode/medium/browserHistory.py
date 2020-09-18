class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.size = 1
        self.current = 0
        

    def visit(self, url: str) -> None:
        self.current += 1
        self.size = self.current + 1
        if self.size > len(self.history):
            self.history.append(url)
        else:
            self.history[self.current] = url
        # print("new history %s" %self.history)

    def back(self, steps: int) -> str:
        # print("go back from %s" %self.current)
        self.current = (0 if steps > self.current else self.current-steps)
        # print("new cur is %s" %self.current)
        return self.history[self.current]
        

    def forward(self, steps: int) -> str:
        # print("go forward from %s" %self.current)
        self.current = (self.size-1 if steps + self.current >= self.size else steps + self.current)
        # print("new cur is %s" %self.current)
        return self.history[self.current]
        
        
        
        
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
