class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def dp(i, holding, remaining):
            if remaining == 0 or i == len(prices):
                return 0
            
            ans = dp(i+1, holding, remaining)
            if holding:
                ans = max(ans, prices[i] + dp(i+1, False, remaining-1))
            else:
                ans = max(ans, -prices[i] + dp(i+1, True, remaining))
                
            return ans
        
        return dp(0, False, k)