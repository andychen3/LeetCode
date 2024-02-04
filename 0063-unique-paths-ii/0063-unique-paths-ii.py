class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * col for _ in range(row)]
        dp[0][0] = 1
        
        for r in range(row):
            for c in range(col):
                if obstacleGrid[r][c] == 1:
                    continue
                if r > 0:
                    dp[r][c] += dp[r-1][c]
                if c > 0:
                    dp[r][c] += dp[r][c-1]
        return dp[row - 1][col -1]
        