class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1
        
        for i in range(3, n + 1):
            dp[i] = dp[i-3] + dp[i-1] + dp[i-2]
        return dp[n]
#         @cache
#         def dp(i):
#             if i == 0:
#                 return 0
            
#             if i == 1 or i == 2:
#                 return 1
            
#             return dp(i-3) + dp(i - 1) + dp(i - 2)
#         return dp(n)