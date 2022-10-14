class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        char_hash = {']': '[', '}': '{', ')':'('}
        
        for char in s:
            if stack and char in char_hash:
                if char_hash[char] == stack[-1]:
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(char)
        
        return not stack