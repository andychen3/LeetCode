class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def check(word):
            stack = []
            
            for char in word:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return "".join(stack)
    
        return check(s) == check(t)
        