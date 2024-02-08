class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [[0] * col for _ in range(row)]
        dp[0][0] = grid[0][0]
        
        for r in range(row):
            for c in range(col):
                if r + c == 0:
                    continue
                ans = float("inf")
                if r > 0:
                    ans = min(ans, dp[r-1][c])
                if c > 0:
                    ans = min(ans, dp[r][c-1])
                dp[r][c] = grid[r][c] + ans
        return dp[row-1][col-1]
    
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
            
#         m, n = len(grid), len(grid[0])
#         return dp(m - 1, n - 1)