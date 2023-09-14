from functools import cache
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def dp(i, remaining, holding):
            if i == len(prices) or remaining == 0:
                return 0

            # do nothing
            skip = dp(i+1, remaining, holding)
            ans = 0
            #recurrence relation
            # I can buy, sell, or do nothing
            if holding: # We have a stock
                ans = prices[i] + dp(i+1, remaining - 1, 0)
            else:
                ans = -prices[i] + dp(i+1, remaining, 1)
            
            return max(ans, skip)

        return dp(0, k, 0)