from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def dp(amount):
            if amount < 0:
                return float("inf")
            if amount == 0:
                return 0
            
            min_coins = float('inf')
            for coin in coins:
                min_coins = min(min_coins, 1 + dp(amount - coin))
            
            return min_coins 
        
        result = dp(amount)
        return result if result != float("inf") else -1


