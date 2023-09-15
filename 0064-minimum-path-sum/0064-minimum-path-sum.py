from functools import cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def dp(row, col):
            # We return grid[row][col] because at the end when we reach end we return the number there
            if row + col == 0:
                return grid[row][col]
            
            ans = float("inf")
            # we want the min of going down
            if row > 0:
                ans = min(ans, dp(row-1, col))
            # we want min of going right
            if col > 0:
                ans = min(ans, dp(row, col -1))
            # We always add whatever the value to the min answer because we are currently there
            return grid[row][col] + ans
            

        m, n = len(grid), len(grid[0])
        return dp(m-1, n-1)