class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for row in range(m):
            for col in range(n):
                if row + col == 0:
                    continue
                if row > 0 and obstacleGrid[row][col] != 1:
                    dp[row][col] += dp[row-1][col]
                if col > 0 and obstacleGrid[row][col] != 1:
                    dp[row][col] += dp[row][col-1]
        return dp[m-1][n-1]
#         @cache
#         def dp(row, col):
#             if row + col == 0:
#                 return 1
            
#             ways = 0
#             if row > 0 and obstacleGrid[row][col] != 1:
#                 ways += dp(row - 1, col)
#             if col > 0 and obstacleGrid[row][col] != 1:
#                 ways += dp(row, col - 1)
#             return ways
#         return dp(m - 1, n - 1)