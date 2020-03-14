def maxProfit(prices):
    bestPrice = 0
    minBuy = maxSell = None
    for price in prices:
        if minBuy is None or minBuy > price:
            minBuy = price
            maxSell = None
            continue
        if maxSell is None or maxSell < price:
            maxSell = price
        if bestPrice < (maxSell - minBuy):
            bestPrice = maxSell - minBuy
    return bestPrice


def maxProfit2(prices):
        if len(prices) == 0:
            return 0
        maxProfit = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
                continue
            if i + 1 < len(prices) and prices[i] < prices[i + 1]:
                continue
            else:
                maxProfit += (prices[i] - minPrice)
                # print(maxProfit)
                if i + 1 < len(prices):
                    minPrice = prices[i + 1]
        return maxProfit


