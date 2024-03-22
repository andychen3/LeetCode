class Solution:
    def removeVowels(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char not in "aeiuo":
                stack.append(char)
        return "".join(stack)