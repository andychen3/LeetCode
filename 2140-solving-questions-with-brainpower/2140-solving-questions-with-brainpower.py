class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            j = i + questions[i][1] + 1
            dp[i] = max(dp[min(j, n)] + questions[i][0], dp[i + 1])
        return dp[0]
#         @cache
#         def dp(i):
#             if i >= len(questions):
#                 return 0
            
#             return max(questions[i][0] + dp(i + questions[i][1] + 1), dp(i + 1))
#         return dp(0)