class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"]": "[", ")": "(", "}": "{"}
        stack = []
        
        for char in s:
            if char in brackets and stack:
                match = stack.pop()
                if brackets[char] != match:
                    return False
            else:
                stack.append(char)
        return not stack