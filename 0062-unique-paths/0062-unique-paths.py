from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # This is a dp problem because its asking for num of possible unique paths and 
        # The types of movements are constrained to only down and right
        @cache
        def dp(row,col):
            if row + col == 0:
                return 1

            ways = 0
            if row > 0:
                # You are coming from the left
                ways += dp(row-1, col)

            if col > 0:
                # You are coming from up
                ways += dp(row, col-1)
            return ways

        return dp(m-1,n-1)