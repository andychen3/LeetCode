class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for c in s:
            if stack and c == stack[-1].swapcase():
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)