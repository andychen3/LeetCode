from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(remain):
            if remain < 0:
                return float("inf")

            if remain == 0:
                return 0

            min_coins = float("inf")
            
            for coin in coins:
                # Recurrence relation
                min_coins = min(min_coins, dp(remain - coin) + 1)

            return min_coins
        
        return dp(amount) if dp(amount) != float("inf") else -1