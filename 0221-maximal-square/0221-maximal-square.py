class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        self.ans = 0
        
        @cache
        def dp(row, col):
            if row >= m or col >= n:
                return 0
            
            length = 0
            if matrix[row][col] == "1":
                length = min(dp(row+1, col), dp(row, col+1), dp(row+1, col+1)) + 1
                self.ans = max(self.ans, length)
            else:
                dp(row+1, col)
                dp(row, col+1)
                dp(row+1, col+1)
            return length
        dp(0,0)
        return self.ans ** 2
            