from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = Counter(s)

        for key in t:
            if key not in s_count or s_count[key] == 0:
                return key
            s_count[key] -= 1
            
        