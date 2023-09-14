from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dp(i):
            # We check for less than 0 because if the first word matches
            # we need to check if the prior word also matches a word in wordDict.
            if i < 0 :
                return True

            for word in wordDict:
                # We check if the word can pontetially form from s and dp(i-len(word)) checks for if
                # previous word was formable
                if i >= len(word) - 1 and dp(i - len(word)):
                    # Recurrence relation?
                    # This builds the string from the end - len of word + 1 because of inclusive and then
                    # builds the length of the word + 1 inclusive again and check if it matches the word
                    if s[i - len(word) + 1: i + 1] == word:
                        return True
            return False
        
        return dp(len(s) - 1) # so we can index into the word