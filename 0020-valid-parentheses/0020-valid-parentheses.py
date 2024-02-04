class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"]": "[", "}": "{", ")": "("}
        stack = []
        
        for char in s:
            if char in brackets and stack:
                matching_bracket = stack.pop()
                if brackets[char] != matching_bracket:
                    return False
            else:
                stack.append(char)
        return not stack