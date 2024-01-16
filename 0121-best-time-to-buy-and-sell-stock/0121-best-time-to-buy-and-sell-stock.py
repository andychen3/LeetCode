class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr = float("inf")
        
        for price in prices:
            curr = min(price, curr)
            profit = max(profit, price - curr)
        return profit