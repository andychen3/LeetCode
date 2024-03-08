class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[inf] * (n) for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        for row in range(m):
            for col in range(n):
                if row + col == 0:
                    continue
                if row > 0:
                    dp[row][col] = min(dp[row][col], dp[row-1][col])
                if col > 0:
                    dp[row][col] = min(dp[row][col], dp[row][col-1] )
                dp[row][col] += grid[row][col] 
        return dp[m-1][n-1]
#         @cache
#         def dp(row, col):
#             if row + col == 0:
#                 return grid[row][col]
            
#             ways = inf
#             if row > 0:
#                 ways = min(ways, dp(row - 1, col))
#             if col > 0:
#                 ways = min(ways, dp(row, col - 1))
#             return grid[row][col] + ways
#         m, n = len(grid), len(grid[0])
#         return dp(m - 1, n - 1)