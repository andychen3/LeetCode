class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dp(i):
            if i < 0:
                return True
            
            for word in wordDict:
                if i == len(word) - 1 or dp(i - len(word)):
                    if s[i - len(word) + 1: i + 1] == word:
                        return True
        return dp(len(s) - 1)