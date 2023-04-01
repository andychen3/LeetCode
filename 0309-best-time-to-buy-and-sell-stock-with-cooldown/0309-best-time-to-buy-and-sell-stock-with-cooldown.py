class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i, holding):
            if i >= len(prices):
                return 0
            
            ans = dp(i+1, holding)
            
            if holding:
                ans = max(prices[i] + dp(i+2, False), ans)
            else:
                ans = max(-prices[i]+ dp(i+1, True), ans)
            return ans
        return dp(0, False)