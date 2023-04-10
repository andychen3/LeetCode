class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {')' :'(', ']': '[', "}": "{"}
        stack = []
        
        for char in s:
            if char in hash_map and stack:
                c = stack.pop()
                if hash_map[char] != c:
                    return False
            else:
                stack.append(char)
        return not stack
                