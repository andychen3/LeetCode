from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dp(i, remain):
            if remain < 0:
                return 0

            if i == len(coins):
                return 0

            if remain == 0:
                return 1
            # Reason why you don't need a for loop because i is used to go through
            # the coins array

            # The recurrence relation is if you take the same coin how many times can you take it
            # If you skip the coin remain stays the same
            ways = dp(i, remain - coins[i]) + dp(i+ 1, remain)
            
            return ways

        return dp(0, amount)