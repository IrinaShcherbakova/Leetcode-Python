class RecentCounter:

    def __init__(self):
        self.requests = deque()
        

    def ping(self, t: int) -> int:
        lower_bound = max(0, t-3000)
        self.requests.append(t)
        while self.requests and self.requests[0] < lower_bound:
            self.requests.popleft()
        return len(self.requests)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
