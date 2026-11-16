class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minB, maxP = prices[0], 0

        for p in prices:
            minB = min(minB, p)
            maxP = max(maxP, p - minB)

        return maxP