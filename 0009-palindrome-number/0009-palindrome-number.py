class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        left, right = 0, len(string) - 1
        
        while left < right:
            left_char = string[left]
            right_char = string[right]
            if left_char != right_char:
                return False
            left += 1
            right -= 1
        return True