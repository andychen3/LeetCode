class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dp(i, j):
            if i >= len(s) and j >= len(p):
                return True
            elif j >= len(p):
                return False
            else:
                match = i < len(s) and (s[i] == p[j] or p[j] == ".")
                if j + 1 < len(p) and p[j + 1] == "*":
                    return dp(i, j + 2) or match and dp(i + 1, j)
                else:
                    return match and dp(i+1, j + 1)
            return False
        return dp(0,0)