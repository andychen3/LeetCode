class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left_ptr = 0
        right_ptr = 0

        while left_ptr < len(s) and right_ptr < len(t):
            if s[left_ptr] == t[right_ptr]:
                left_ptr += 1
            right_ptr += 1
        
        return left_ptr == len(s)