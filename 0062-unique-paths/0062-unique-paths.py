class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # This is a dp problem because its asking for num of possible unique paths and 
        # The types of movements are constrained to only down and right
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for row in range(m):
            for col in range(n):
                # We are iterating forward and making sure that row is not negative because
                # we start from 0,0
                if row > 0:
                    dp[row][col] += dp[row-1][col]
                if col > 0:
                    dp[row][col] += dp[row][col-1]

        return dp[m-1][n-1]
