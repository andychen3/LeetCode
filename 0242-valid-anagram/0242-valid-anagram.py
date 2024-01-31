from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counts = Counter(s)
        
        for char in t:
            if char not in s_counts:
                return False
            else:
                s_counts[char] -= 1
                if s_counts[char] == 0:
                    del s_counts[char]
        return True