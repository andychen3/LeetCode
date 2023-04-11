from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pattern = Counter(s1)
        left = 0
        
        for right, word in enumerate(s2):
            pattern[word] -= 1
                
            while pattern[word] < 0:
                left_word = s2[left]
                pattern[left_word] += 1
                left += 1
            
            if right - left + 1 == len(s1):
                return True
        return False