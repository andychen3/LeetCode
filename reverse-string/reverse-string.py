class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            left_char = s[left]
            right_char = s[right]
            s[left], s[right] = right_char, left_char
            left += 1
            right -= 1
            
        return s