class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy, maxP = prices[0], 0

        for p in prices:
            minBuy = min(p, minBuy)
            maxP = max(maxP, p - minBuy)

        return maxP