class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        memo = [[0] * col for _ in range(row)]
        
        def dp(r, c, pre):
            if r < 0 or r >= row or c < 0 or c >= col or matrix[r][c] <= pre:
                return 0
            
            if memo[r][c]:
                return memo[r][c]
            
            ans = 1
            ans = max(ans, 1 + dp(r + 1, c, matrix[r][c]))
            ans = max(ans, 1 + dp(r , c - 1, matrix[r][c]))
            ans = max(ans, 1 + dp(r - 1, c, matrix[r][c]))
            ans = max(ans, 1 + dp(r , c + 1, matrix[r][c]))
            memo[r][c] = ans
            return ans
        
        ans = 0
        for x in range(row):
            for y in range(col):
                ans = max(ans, dp(x, y, -1)) 
        return ans
        
#         row, col = len(matrix), len(matrix[0])
        
#         @cache
#         def dp(r, c, pre):
#             if r < 0 or r >= row or c < 0 or c >= col or matrix[r][c] <= pre:
#                 return 0
            
#             ans = 1
#             ans = max(ans, 1 + dp(r + 1, c, matrix[r][c]))
#             ans = max(ans, 1 + dp(r , c - 1, matrix[r][c]))
#             ans = max(ans, 1 + dp(r - 1, c, matrix[r][c]))
#             ans = max(ans, 1 + dp(r , c + 1, matrix[r][c]))
#             return ans
        
#         ans = 0
#         for x in range(row):
#             for y in range(col):
#                 ans = max(ans, dp(x, y, -1)) 
#         return ans
        