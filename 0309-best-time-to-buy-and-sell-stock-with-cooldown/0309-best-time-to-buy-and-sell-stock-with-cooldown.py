from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i, holding):
            if i >= len(prices):
                return 0

            skip = dp(i+1, holding)
            do_something = 0

            if holding:
                do_something = prices[i] + dp(i+2, 0)
            else:
                do_something = -prices[i] + dp(i+1, 1)
            
            return max(do_something, skip)
        
        return dp(0, 0)
        