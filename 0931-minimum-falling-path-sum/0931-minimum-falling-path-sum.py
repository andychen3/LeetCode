class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        @cache
        def dp(row, col):
            if row < 0 or row >= n or col < 0 or col >= n:
                return inf
            
            if row == n - 1:
                return matrix[row][col]
            
            return matrix[row][col] + min(
            dp(row + 1, col -1),
            dp(row+1, col),
            dp(row+1, col+1))
        return min(dp(0, col) for col in range(n))
            