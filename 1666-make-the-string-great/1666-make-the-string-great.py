class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        stack = []
        
        for char in s:
            if stack and stack[-1].swapcase() == char:
                stack.pop()
            else:
                stack.append(char)
        
        return ''.join(stack)