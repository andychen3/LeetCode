class Solution:
    def climbStairs(self, n: int) -> int:
        # This covers base cases that if n = 1 you take 1 step and if n =2 you take 2 steps total
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        print(dp)
        return dp[n]