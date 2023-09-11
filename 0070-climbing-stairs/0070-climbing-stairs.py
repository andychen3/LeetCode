class Solution:
    def climbStairs(self, n: int) -> int:
        # this is a dp problem only because i have seen it. and it is asking how many distinct ways
        # So there are overlapping subproblems
        dp = [1] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
