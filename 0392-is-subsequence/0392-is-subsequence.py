class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) == 0 and len(s) != 0:
            return False
        if len(s) == 0 and len(t) != 0:
            return True
        
        left = 0
        
        for right, char in enumerate(t):
            if left < len(s) and char == s[left]:
                left += 1
        
        return left == len(s)