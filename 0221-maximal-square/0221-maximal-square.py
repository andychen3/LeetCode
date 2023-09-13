from functools import cache
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        @cache
        def dp(row, col):
            if row >= n or col >= m:
                return 0
            val = 0
            # IS it a one or not a one
            if matrix[row][col] == '1':
                # up, left, top left / You add 1 because because a square can only be limited
                # by its shortest side. Then you add 1 to extend it
                val = min(dp(row+1, col), dp(row, col + 1), dp(row+1, col+1)) + 1
                self.ans = max(self.ans, val)
            else:
                dp(row+1, col), dp(row, col + 1), dp(row+1, col+1)
            return val            
        
        self.ans = 0
        n, m = len(matrix), len(matrix[0])
        dp(0,0)
        return self.ans * self.ans 