class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0] * (k + 1) for _ in range(2)] for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for remaining in range(1, k + 1):
                for holding in range(2):
                    ans = dp[i + 1][holding][remaining]
                    if holding:
                        ans = max(ans, prices[i] + dp[i+1][0][remaining - 1])
                    else:
                        ans = max(ans, -prices[i] + dp[i + 1][1][remaining])
                    dp[i][holding][remaining] = ans
        return dp[0][0][k]
        
        
#         @cache
#         def dp(i, holding, remain):
#             if i >= len(prices) or remain == 0:
#                 return 0
            
#             ans = dp(i + 1, holding, remain)
#             if holding:
#                 ans = max(ans, prices[i] + dp(i + 1, False, remain - 1))
#             else:
#                 ans = max(ans, -prices[i] + dp(i + 1, True, remain))
                
#             return ans
            
#         return dp(0, 0, k)