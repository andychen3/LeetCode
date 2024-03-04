from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        count_s = Counter(s)
        
        for char in t:
            if char in count_s:
                count_s[char] -= 1
                if count_s[char] == 0:
                    del count_s[char]
            else:
                return False
        return True