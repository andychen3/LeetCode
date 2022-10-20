class Solution:
    def reverseString(self, s: List[str], start=None, end=None) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if start == None and end == None:
            start = 0
            end = len(s)-1
        
        if start >= end:
            return
        
        s[start], s[end] = s[end], s[start]
        self.reverseString(s, start+1, end-1)
        