from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(curr):
            if curr == 0:
                return 0

            min_coins = float("inf")
            for c in coins:
                if curr - c >= 0:
                    min_coins = min(min_coins, 1 + dp(curr - c))
            return min_coins
        
        result = dp(amount)
        return result if result != float("inf") else -1
