class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
#         n = len(coins)
#         dp = [[0] * (amount + 1) for _ in range(n + 1)]
        
#         for i in range(n+1):
#             dp[i][0] = 1
            
#         for i in range(n - 1, -1, -1):
#             for remain in range(amount + 1):
#                 if remain - coins[i] >= 0:
#                     dp[i][remain] = dp[i][remain-coins[i]] + dp[i+1][remain]
#                 else:
#                     dp[i][remain] = dp[i+1][remain]
#         return dp[0][amount]
        
        
        @cache
        def dp(remaining, i):
            if i == len(coins) or remaining < 0:
                return 0
            if remaining == 0:
                return 1
            return dp(remaining - coins[i], i) + dp(remaining, i + 1)
        return dp(amount, 0)
            