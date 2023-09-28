class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        # We do n // 2 because any string that is more than half won't match.
        for i in range(1, n // 2 + 1):
            # We check if it's an even string because if odd it won't work
            if n % i == 0:
                # We build the substring from the start to the current index and multiply it
                # by how many times to get the length of s
                substring = s[:i] * (n // i)
                if substring == s:
                    return True
        return False
                