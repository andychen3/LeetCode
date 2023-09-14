class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # False because we are trying to return true or false
        dp = [False] * len(s)

        for i in range(len(s)):
            for word in wordDict:
                # We first chceck if length of s is greater than a length of a word
                # WE have the condition to check if i is equal to length of a word in wordDict
                # This is to check for if the first word is built from 0 to i and there is no previous word
                # because dp[i-len(word)] would be negative and that is out of bounds
                # After we have found a word dp[i-len(word)] would check if the previous word was true
                if i >= len(word) - 1 and (i == len(word) - 1 or dp[i - len(word)]):
                    if s[i - len(word) + 1 : i + 1] == word:
                        dp[i] = True
                        break

        return dp[-1]

        