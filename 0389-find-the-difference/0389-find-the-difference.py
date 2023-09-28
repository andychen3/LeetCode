from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = Counter(s)
        t_count = Counter(t)

        for key, val in t_count.items():
            if s_count[key] != val:
                return key
            elif key not in s_count:
                return key
        