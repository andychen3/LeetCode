class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"]": "[", "}": "{", ")": "("}
        stack = []
        
        for char in s:
            if char in brackets and stack:
                matching = stack.pop()
                
                if brackets[char] != matching:
                    return False
            else:
                stack.append(char)
        return not stack