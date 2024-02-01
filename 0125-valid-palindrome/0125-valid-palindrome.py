class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        left, right = 0, len(string) - 1
        
        while left <= right:
            left_char = string[left]
            right_char = string[right]
            
            if left_char == right_char:
                left += 1
                right -= 1
            elif not left_char.isalnum():
                left += 1
            elif not right_char.isalnum():
                right -= 1
            else:
                return False
        return True
        