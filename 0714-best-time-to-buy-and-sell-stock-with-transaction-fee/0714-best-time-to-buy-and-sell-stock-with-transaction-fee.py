class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0,0] for _ in range(n+1)]
        
        for i in range(n-1, -1, -1):
            for holding in range(2):
                ans = dp[i+1][holding]
                if holding:
                    ans = max(ans, prices[i] + dp[i+1][0] - fee)
                else:
                    ans = max(ans, -prices[i] + dp[i+1][1])
                dp[i][holding] = ans
        return dp[0][0]
        
#         @cache
#         def dp(i, holding):
#             if i >= len(prices):
#                 return 0
            
#             ans = dp(i+1, holding)
#             if holding:
#                 ans = max(ans, prices[i] + dp(i+1, False) - fee)
#             else:
#                 ans = max(ans, -prices[i] + dp(i+1, True))
#             return ans
#         return dp(0,0)