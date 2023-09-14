class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices = float("inf")
        best = 0
        for num in prices:
            min_prices = min(num, min_prices)
            best = max(best, num - min_prices)
        return best