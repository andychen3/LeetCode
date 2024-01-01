from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = Counter(s)
        
        for char in t:
            if char in counts and counts[char] > 0:
                counts[char] -= 1
            else:
                return False
        return True