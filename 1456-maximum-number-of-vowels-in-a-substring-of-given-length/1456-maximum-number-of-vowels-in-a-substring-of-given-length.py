class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 0
        left = 0
        max_vowels = 0
        
        for right, letter in enumerate(s):
            if letter in 'aeiou':
                vowels += 1
            
            while right - left >= k:    
                if s[left] in "aeiou":
                    vowels -= 1
                left += 1
        
            max_vowels = max(max_vowels, vowels)
        
        return max_vowels