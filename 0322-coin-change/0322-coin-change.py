from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(curr):
            # We set curr to == 0 because it takes 0 coins to make a total of 0
            if curr < 0:
                return float("inf")
            if curr == 0:
                return 0

            # we set min coins to create amount to a huge number
            min_coins = float("inf")
            for c in coins:
                    # If so we find the minimum amount of coins it takes to create the amount
                    # we add 1 to dp because everytime you take a coin you add 1 to the min amount
                    # of coins.
                min_coins = min(min_coins, 1 + dp(curr - c))
            return min_coins
        
        result = dp(amount)
        return result if result != float("inf") else -1
