from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def dp(amount):
            # amount == 0 return 0 because when the amount is 0 we don't need any coins
            # to form 0
            if amount == 0:
                return 0
            
            # We set the starting number of coints to an arbitrary large number
            min_coins = float('inf')
            for coin in coins:
                # This recurrence relationship tries to solve the minimum number of coins to
                # create the amount.
                # we add 1 + dp(amount-coin) because when a total can be made it takes 1 coin.
                if amount - coin >= 0:
                    min_coins = min(min_coins, 1 + dp(amount - coin))
            
            return min_coins 
        
        # We do this part because the answer can be float(inf) that is returned which means
        # there is no answer thus it should be changed to -1
        result = dp(amount)
        return result if result != float("inf") else -1


