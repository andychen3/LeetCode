from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # what do i want my function to return? I want it to return the fewest number of coins
        # What is my state variable. curr to track the amount 
        # What is my recurrence relation? My recurrence relation is.... 
        @cache
        def dp(curr):
            # If the curr sum is invalid. We return a huge coin value
            # Because this answer is not possible
            if curr < 0:
                return float("inf")
            # If we get the curr sum to equal amount that means we found a solution.
            # We return 0 because when the recursion returns it already adds 1 to the possible solution
            if curr == 0:
                return 0

            min_coins = float("inf") # We float inf because we want the fewest num of coins
            for c in coins:
                min_coins = min(min_coins, 1 + dp(curr - c))
            
            return min_coins if min_coins != float("inf") else float("inf")
        
        result = dp(amount)
        return result if result != float("inf") else -1