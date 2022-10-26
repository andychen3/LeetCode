class Solution:
    def makeGood(self, s: str) -> str:
        if not s:
            return ""
        
        stack = []
        
        for char in s:
            if stack:
                if char == char.upper() and stack[-1] == char.lower():
                    stack.pop()
                    continue
                elif char == char.lower() and stack[-1] == char.upper():
                    stack.pop()
                    continue
            stack.append(char)
        
        return "".join(stack)
        