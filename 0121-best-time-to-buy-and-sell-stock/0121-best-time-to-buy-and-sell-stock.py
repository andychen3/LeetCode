class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices = float("inf")
        best = 0
        for num in prices:
            # You try to find the min_price to sell
            min_prices = min(num, min_prices)
            # You find the best price from wherever you are selling to the min_price
            best = max(best, num - min_prices)
        return best