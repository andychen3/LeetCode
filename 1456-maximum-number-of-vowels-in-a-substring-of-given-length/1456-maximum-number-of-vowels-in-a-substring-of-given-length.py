
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        left = 0
        vowels = 0
        
        for right, char in enumerate(s):
            if char in 'aeiou':
                vowels += 1
                
            while right - left + 1 > k:
                if s[left] in 'aeiou':
                    vowels -= 1
                left += 1
                
            
            res = max(res, vowels)
        
        return res
                