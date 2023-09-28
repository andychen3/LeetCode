from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_char = Counter(s)

        for char in t:
            if char in s_char and s_char[char] > 0:
                s_char[char] -= 1
            else:
                return False
        return True
        