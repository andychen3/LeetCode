class Solution:
    def climbStairs(self, n: int) -> int:
        # this is a dp problem only because i have seen it. and it is asking how many distinct ways
        # So there are overlapping subproblems
        # The reason i defined everything as 1 instead of 0 is because we are trying to find
        # the amouint of distinct ways. At every instance whether or not you take 1 or 2 steps that counts
        # as a way. The recurrence relation is the adding of these two distinct ways. 
        # By doing it this way I don't have to do dp[0], dp[1], dp[2] to set to 1.
        dp = [1] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
