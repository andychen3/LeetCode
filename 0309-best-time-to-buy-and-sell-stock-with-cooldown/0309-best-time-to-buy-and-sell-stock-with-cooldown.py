class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * (2) for _ in range(n+1)]
        
        for i in range(n-1, -1, -1):
            for holding in range(2):
                dp[i][holding] = dp[i+1][holding]
                if holding:
                    dp[i][holding] = max(dp[i][holding], prices[i] + dp[min(i + 2, n)][False])
                else:
                    dp[i][holding] = max(dp[i][holding], -prices[i] + dp[i + 1][True])
        return dp[0][False]
        
#         @cache
#         def dp(i, holding):
#             if i >= len(prices):
#                 return 0
            
#             ans = dp(i+1, holding)
#             if holding:
#                 ans = max(ans, prices[i] + dp(i+2, False))
#             else:
#                 ans = max(ans, -prices[i] + dp(i+1, True))
                
#             return ans
        
#         return dp(0, False)
        