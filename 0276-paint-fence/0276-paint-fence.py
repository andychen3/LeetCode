class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k

        if n == 2:
            return k * k

        dp = [0] * (n + 1)
        # We skip dp[0] because when you have zero posts there are 0 ways to paint it
        dp[1] = k
        dp[2] = k * k

        for i in range(3, n + 1):
            dp[i] = (k-1) * (dp[i-1] + dp[i-2])
        print(dp)
        return dp[n]       
 