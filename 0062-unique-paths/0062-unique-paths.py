class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
        return dp[m-1][n-1]
#         @cache
#         def dp(row, col):
#             if row == 0 and col == 0:
#                 return 1
            
#             ans = 0
#             if row > 0:
#                 ans += dp(row-1, col)
#             if col > 0:
#                 ans += dp(row, col - 1)
#             return ans
#         return dp(m-1,n-1)
            