from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(remain):
            # base case because if the subtracted amount is less than 0
            # Then we return an arb high number to tell that this is an invalid solution
            if remain < 0:
                return float("inf")

            # Since we are always subtracting the coin amount from the remainder we will get a function call
            # That could equal 0. In that case that means we found a valid answer and since we don't need
            # anymore coins. We can return 0 which indicates that we need 0 coins to make 0 amount
            if remain == 0:
                return 0

            # Because we are finding the min fewest coin. In order for the recurrence relation to work
            # We need to set the starting point to an arb high number and continuously update this
            # as we find the fewest possible coins to make up amount
            min_coins = float("inf")
            
            # Iterate through the coins given
            for coin in coins:
                # Recurrence relation
                # So we compare min_coins which is originally set to an arb high value and our second
                # choice is that if we can take this coin. WE must subtract it from the remaining amount.
                # if it is a valid solution we add 1 to it because that means we can take this coin. 
                min_coins = min(min_coins, dp(remain - coin) + 1)

            return min_coins
        
        # We have to cover the case that if there is no combination to return -1
        # This is why if dp(amount) comes back as float("inf") based on our base case
        # That means there was no valid combination found.
        return dp(amount) if dp(amount) != float("inf") else -1