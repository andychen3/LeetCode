class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (amount + 1)
        dp[0] = 0
        
        for c in coins:
            for remaining in range(c, amount + 1):
                dp[remaining] = min(dp[remaining - c] + 1, dp[remaining])
        return dp[amount] if dp[amount] != inf else -1
#         @cache
#         def dp(remaining):
#             if remaining < 0:
#                 return inf
#             if remaining == 0:
#                 return 0
#             ans = inf
            
#             for c in coins:
#                 ans = min(ans, dp(remaining - c) + 1)
#             return ans
#         return dp(amount) if dp(amount) != inf else -1