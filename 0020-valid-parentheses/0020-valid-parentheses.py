class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")" : "(", "]": "[", "}": "{"}
        stack = []
        
        for char in s:
            if char in brackets and stack:
                open_bracket = stack.pop()
                if brackets[char] != open_bracket:
                    return False
            else:
                stack.append(char)
        return not stack