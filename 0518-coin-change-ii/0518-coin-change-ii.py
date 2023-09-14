class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (n+1) for _ in range(amount + 1)]

        # We have to iterate through and set the columns to 1 because on the zeroth coin
        # You can create 0 coin with 1 coin. 
        # The reason why you can't set all the initial values to 1 is because it is not true that you can build
        # any coin with 1 coin if that coin is not in your coins list.
        for i in range(n+1):
            dp[0][i] = 1


        for remain in range(amount+1):
            for i in range(n -1, -1, -1):
                # We do the recurrence relation only if remain - coin is either equal to 0 or there is
                # still remain left to find another coin
                if remain - coins[i] >= 0:
                    dp[remain][i] = dp[remain - coins[i]][i] + dp[remain][i+1]
                # We have to have this else statement because if the coin is bigger than remain that 
                # means it will be an invalid solution so we must skip it and move on
                else:
                    dp[remain][i] = dp[remain][i+1]
        
        print(dp)
        return dp[amount][0]
