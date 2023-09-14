class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        # We go forward because we are trying to reach the bottom right corner
        for row in range(m):
            for col in range(n):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                    continue
                # Check if we aren't negative
                if row > 0:
                    # check how many steps were from the left
                    dp[row][col] += dp[row-1][col]
                if col > 0:
                    # check how many steps were from the up
                    dp[row][col] += dp[row][col-1]

        return dp[m-1][n-1]
        