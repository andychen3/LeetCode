from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pattern = Counter(p)
        ans = []
        left = 0
        
        for right, char in enumerate(s):
            pattern[char] -= 1
            
            while pattern[char] < 0:
                pattern[s[left]] += 1
                left += 1
            
            if right - left + 1 == len(p):
                ans.append(left)
        return ans