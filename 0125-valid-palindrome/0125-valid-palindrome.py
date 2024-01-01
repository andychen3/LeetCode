class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = s.lower()
        left, right = 0, len(word) - 1
        
        while left < right:
            if word[left] == word[right]:
                left += 1
                right -= 1
            elif not word[left].isalnum():
                left += 1
            elif not word[right].isalnum():
                right -= 1
            else:
                return False
        return True