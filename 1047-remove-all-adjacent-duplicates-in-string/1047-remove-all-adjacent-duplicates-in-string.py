class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for c in s:
            if stack:
                if stack[-1] == c:
                    stack.pop()
                    continue
            stack.append(c)
                
        return "".join(stack)