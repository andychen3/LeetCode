class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        # We subtract out the length of needle because if there is a valid needle in haystack
        # it will always end n - m.
        for start in range(n - m + 1): 
            # Iterate through the length of needle and compare chars
            # if it doesn't match break out and find new start
            for i in range(m):
                if needle[i] != haystack[start + i]:
                    break
                # if i is at the end and this loop hasn't broke yet that means
                # We found an answer return the start index
                if i == m - 1:
                    return start
        return -1