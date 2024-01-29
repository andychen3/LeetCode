class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(remaining):
            if remaining < 0:
                return float("inf")
            if remaining == 0:
                return 0
            
            min_coins = float("inf")
            for c in coins:
                min_coins = min(min_coins, dp(remaining - c) + 1)
            return min_coins
        return dp(amount) if dp(amount) != float("inf") else -1