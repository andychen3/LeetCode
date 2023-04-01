class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(left, right):
            if left + right == 2*n:
                ans.append("".join(stack))
                return
            
            if left < n:
                stack.append("(")
                backtrack(left + 1, right)
                stack.pop()
                
            if right < left:
                stack.append(")")
                backtrack(left, right + 1)
                stack.pop()
        
        stack = []
        ans = []
        backtrack(0, 0)
        return ans