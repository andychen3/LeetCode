class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def mod_string(word):
            stack = []
            
            for char in word:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return "".join(stack)
        return mod_string(s) == mod_string(t)