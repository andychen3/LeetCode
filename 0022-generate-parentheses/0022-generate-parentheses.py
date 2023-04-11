class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(stack, left, right):
            if left + right == 2*n:
                return self.ans.append("".join(stack[:]))
            if left < n:
                stack.append("(")
                backtrack(stack, left + 1, right)
                stack.pop()
            if right < left:
                stack.append(")")
                backtrack(stack, left, right+1)
                stack.pop()
            
        self.ans = []
        backtrack([], 0, 0)
        return self.ans