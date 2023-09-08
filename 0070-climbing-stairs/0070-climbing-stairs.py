class Solution:
    def climbStairs(self, n: int) -> int:
        # This covers base cases that if n = 1 you take 1 step and if n =2 you take 2 steps total
        if n <= 2:
            return n

        dp = [0] * (n + 1) # We do n + 1 because we want the answer at the end
        dp[0] = 0 # On the floor
        dp[1] = 1 # if there is only one step
        dp[2] = 2 # If there are two steps. You can do 1 + 1 or 2 which totals to 2

        for i in range(3, n + 1): # Start from 3 because we defined our base cases
            # We are adding the total number of ways using 1 step and 2 step
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]