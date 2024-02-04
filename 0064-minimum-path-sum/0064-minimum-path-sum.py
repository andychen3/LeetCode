class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = grid[0][0]
        
        for row in range(rows):
            for col in range(cols):
                if row + col == 0:
                    continue
                ans = float("inf")
                if row > 0:
                    ans = min(ans, dp[row - 1][col])
                if col > 0:
                    ans = min(ans, dp[row][col - 1])
                dp[row][col] = grid[row][col] + ans
        return dp[rows - 1][cols - 1]
        
        
#         @cache
#         def dp(row, col):
#             if row + col == 0:
#                 return grid[row][col]
            
#             ans = float("inf")
#             if row > 0:
#                 ans = min(ans, dp(row - 1, col))
#             if col > 0:
#                 ans = min(ans, dp(row, col - 1))
#             return grid[row][col] + ans
#         return dp(len(grid) - 1, len(grid[0]) - 1)
            