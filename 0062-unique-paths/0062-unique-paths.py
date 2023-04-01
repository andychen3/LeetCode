class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dp(row, col):
            if row == m or col == n:
                return 0
            
            if (row, col) == (m-1, n-1):
                return 1
            
                        
            
            return dp(row+1, col) + dp(row, col+1)
        
        return dp(0,0)