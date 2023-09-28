class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        for start in range(n - m + 1): # We subtract out the length of needle
            for i in range(m):
                if needle[i] != haystack[start + i]:
                    break
                if i == m - 1:
                    return start
        return -1