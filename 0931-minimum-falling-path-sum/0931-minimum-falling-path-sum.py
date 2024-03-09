class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[inf] * (n + 1) for _ in range(n +1)]
        
        for i in range(n):
            dp[n-1][i] = matrix[n-1][i]
            
        for row in range(n-2, -1, -1):
            for col in range(n):
                dp[row][col] = matrix[row][col] + min(
                dp[row+1][col - 1] if col - 1 >= 0 else inf,
                dp[row+1][col],
                   dp[row+1][col+1] if col + 1 < n else inf)
                   
        return min(dp[0])
        
#         @cache
#         def dp(row, col):
#             if row < 0 or row >= n or col < 0 or col >= n:
#                 return inf
            
#             if row == n - 1:
#                 return matrix[row][col]
            
#             return matrix[row][col] + min(
#             dp(row + 1, col -1),
#             dp(row+1, col),
#             dp(row+1, col+1))
#         return min(dp(0, col) for col in range(n))
            