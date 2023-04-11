from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pattern = Counter(p)
        ans = []
        left = 0
        
        for right, word in enumerate(s):
            
            pattern[word] -= 1
            
            while pattern[word] < 0:
                left_word = s[left]
                pattern[left_word] += 1
                left += 1
            
            if right - left + 1 == len(p):
                ans.append(left)
        return ans
            