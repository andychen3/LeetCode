class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(stack, opening, closing):
            if len(stack) == 2 * n:
                ans.append("".join(stack))
                return
            
            if opening < n:
                stack.append("(")
                backtrack(stack, opening + 1, closing)
                stack.pop()
            if closing < opening:
                stack.append(")")
                backtrack(stack, opening, closing + 1)
                stack.pop()
            
        ans = []
        backtrack([], 0, 0)
        return ans