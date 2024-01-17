class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowered_string = s.lower()
        left, right = 0, len(lowered_string) - 1
        
        while left < right:
            left_char = lowered_string[left]
            right_char = lowered_string[right]
            
            if not left_char.isalnum():
                left += 1
            elif not right_char.isalnum():
                right -= 1
            elif left_char == right_char:
                left += 1
                right -= 1
            else:
                return False
        return True
                