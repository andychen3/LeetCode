class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        self.ans = 0
        @cache
        def dp(row, col):
            if row >= m or col >= n:
                return 0
            val = 0
            if matrix[row][col] == "1":
                val = min(dp(row+1,col), dp(row, col+1), dp(row+1, col+1)) + 1
                self.ans = max(self.ans, val)
            else:
                dp(row+1, col)
                dp(row, col + 1)
                dp(row+1, col+1)
            return val
        dp(0,0)
        return self.ans**2