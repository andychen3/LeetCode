from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dp(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            # Both chars can either be the same or not. if not you want to find
            # the max of each path
            if text1[i] == text2[j]:
                return 1 + dp(i+1, j+1)
            
            return max(dp(i, j+1), dp(i+1, j))

        return dp(0, 0)