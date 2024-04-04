class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        ans = 0
        
        for c in s:
            if c == "(":
                stack.append("(")
            elif c == ")":
                stack.pop()
            ans = max(ans, len(stack))
        return ans