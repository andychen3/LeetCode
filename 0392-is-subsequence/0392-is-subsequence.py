from functools import cache
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        @cache
        def dp(i, j):
            if i >= len(s):
                return True
            
            if j >= len(t):
                return False
            
            if s[i] == t[j]:
                return dp(i+1, j+1)
            else:
                return dp(i, j+1)
        return dp(0,0)