class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def remove_backspace(string):
            stack = []
            
            for char in string:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return "".join(stack)
        
        return remove_backspace(s) == remove_backspace(t)