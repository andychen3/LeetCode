class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def dp(i, holding, remaining):
            if i >= len(prices) or remaining == 0:
                return 0
            
            
            ans = dp(i+1, holding, remaining)
            if holding:
                ans = max(ans, prices[i] + dp(i+1, 0, remaining - 1))
            else:
                ans = max(ans, -prices[i] + dp(i+1, 1, remaining))
            return ans
            
        return dp(0, 0, k)