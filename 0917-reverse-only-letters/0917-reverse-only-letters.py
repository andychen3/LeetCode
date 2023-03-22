class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        new_array = list(s)
        left = 0
        right = len(new_array) - 1
        
        while left < right:
            left_char = new_array[left]
            right_char = new_array[right]
            
            if left_char.isalpha() and right_char.isalpha():
                new_array[left], new_array[right] = new_array[right], new_array[left]
                left += 1
                right -= 1
            
            if not left_char.isalpha():
                left += 1
                
            if not right_char.isalpha():
                right -= 1
        
        return "".join(new_array)