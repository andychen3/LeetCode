from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pattern = Counter(s1)
        left = 0
        
        for right, char in enumerate(s2):
            pattern[char] -= 1
            
            while pattern[char] < 0:
                pattern[s2[left]] += 1
                left += 1
                
            if right - left + 1 == len(s1):
                return True
        return False