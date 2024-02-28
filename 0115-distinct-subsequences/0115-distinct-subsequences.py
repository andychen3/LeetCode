class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[0] * (m+1) for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][m] = 1
            
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                dp[i][j] = dp[i+1][j]
                
                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]
        return dp[0][0]
        
        
        # @cache
        # def dp(i, j):
        #     if j == len(t):
        #         return 1
        #     if i == len(s):
        #         return 0
        #     if s[i] == t[j]:
        #         return dp(i+1, j+1) + dp(i+1, j)
        #     else:
        #         return dp(i+1, j)
        # return dp(0,0)
    