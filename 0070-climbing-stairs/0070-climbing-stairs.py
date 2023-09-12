class Solution:
    def climbStairs(self, n: int) -> int:
        # This is the correct solution and the other solutions are wrong even though they work
        # We return n == 1 to cover the edge case if n == 1
        if n == 1:
            return 1
        
        # An array that represents the answer to the problem for a given state
        # We create an array of 0's because this problem is similar to the fib sequence
        # The base cases are that at step 1 it takes 1 step and for step 2 it takes 2 ways
        # 1 + 1 or 2.
        dp = [0] * (n + 1)
        dp[1] = 1 # Base cases
        dp[2] = 2 # Base cases
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] # Recurrence relation

        
        return dp[n]