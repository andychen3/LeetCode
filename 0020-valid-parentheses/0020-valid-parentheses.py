class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {")": "(", "]": "[", "}":"{"}

        for c in s:
            if c in matching:
                if not stack:
                    return False
                
                previous = stack.pop()
                if matching[c] != previous:
                    return False
            else:
                stack.append(c)
        return not stack