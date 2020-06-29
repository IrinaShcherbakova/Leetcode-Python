class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        minIndex = len(prices) - 1
        res = [0] * len(prices)
        res[-1] = prices[minIndex]
        for i in range(len(prices)-2, -1, -1):
            if prices[i] < prices[minIndex]:
                minIndex = i
                res[i] = prices[i]
            else:
                res[i] = prices[i] - self.findDiscount(i, minIndex, prices)
        return res
    
    
    def findDiscount(self, start: int, end: int, prices: List[int]) -> int:
        curPrice = prices[start]
        # print(prices)
        # print(curPrice)
        # print("min Index is at %s" % end)
        for i in range(start+1, end):
            # print(prices[i])
            if prices[i] <= curPrice:
                return prices[i]
        return prices[end]
