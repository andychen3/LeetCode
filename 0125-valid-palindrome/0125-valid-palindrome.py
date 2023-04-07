class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        
        while left < right:
            left_char = s[left].lower()
            right_char = s[right].lower()
            
            if left_char.isalnum() and right_char.isalnum() and left_char != right_char:
                return False
            
            if left_char.isalnum() and right_char.isalnum() and left_char == right_char:
                left += 1
                right -= 1
            
            if not left_char.isalnum():
                left += 1
                
            if not right_char.isalnum():
                right -= 1
                
        
        return True