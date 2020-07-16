class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        span = 1
        while len(self.prices) > 0:
            curPrice, curSpan = self.prices[-1]
            if curPrice <= price:
                self.prices.pop()
                span += curSpan
            else:
                break
        self.prices.append((price,span))
        return span
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
