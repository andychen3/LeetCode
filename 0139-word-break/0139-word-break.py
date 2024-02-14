class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * n
        
        for i in range(n):
            for word in wordDict:
                if i < len(word) - 1:
                    continue
                if i == len(word) - 1 or dp[i - len(word)]:
                    if s[i - len(word) + 1: i + 1] == word:
                        dp[i] = True
                        break
        return dp[n-1]
        
#         @cache
#         def dp(i):
#             if i < 0:
#                 return True
            
#             for word in wordDict:
#                 if i == len(word) - 1 or dp(i - len(word)):
#                     if s[i - len(word) + 1: i + 1] == word:
#                         return True
#         return dp(len(s) - 1)