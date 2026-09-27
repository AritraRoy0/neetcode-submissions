class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy, maxP = prices[0], 0

        for price in prices:
            minBuy = min(minBuy, price)
            maxP = max(price - minBuy, maxP)
        return maxP
        