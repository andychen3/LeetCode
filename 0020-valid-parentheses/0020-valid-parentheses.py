class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"]": "[", "}": "{", ")": "("}
        stack = []
        
        for char in s:
            if stack and char in brackets:
                match = stack.pop()
                if brackets[char] != match:
                    return False
            else:
                stack.append(char)
        return not stack