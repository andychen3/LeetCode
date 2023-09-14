from functools import cache
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        @cache
        def dp(row, col):
            # Base cases
            if row + col == 0:
                return 1
            
            if obstacleGrid[row][col] == 1:
                return 0

            ways = 0
            # Recurrence relation
            if row > 0:
                ways += dp(row-1, col)
            if col > 0:
                ways += dp(row, col-1)
            return ways
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        return dp(m-1, n-1)