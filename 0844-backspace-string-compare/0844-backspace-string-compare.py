class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def parse(string):
            stack = []
            
            for char in string:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return "".join(stack)
        
        return parse(s) == parse(t)