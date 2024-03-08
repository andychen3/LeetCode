class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        @cache
        def dp(row, col):
            if row + col == 0:
                return 1
            
            ways = 0
            if row > 0 and obstacleGrid[row][col] != 1:
                ways += dp(row - 1, col)
            if col > 0 and obstacleGrid[row][col] != 1:
                ways += dp(row, col - 1)
            return ways
        return dp(m - 1, n - 1)