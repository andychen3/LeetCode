class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for remain in range(coin, amount + 1):
                dp[remain] = min(dp[remain], dp[remain - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1
        
#         @cache
#         def dp(remain):
#             if remain == 0:
#                 return 0
#             if remain < 0:
#                 return float("inf")
            
#             ans = float("inf")
#             for coin in coins:
#                 ans = min(ans, dp(remain - coin) + 1)
#             return ans
        
#         return dp(amount) if dp(amount) != float("inf") else - 1