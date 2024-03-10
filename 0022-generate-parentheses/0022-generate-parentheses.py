class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(arr, open_, close):
            if open_ + close == 2 * n:
                ans.append("".join(arr[:]))
                return
            
            if open_ < n:
                arr.append("(")
                backtrack(arr, open_ + 1, close)
                arr.pop()
                
            if close < open_:
                arr.append(")")
                backtrack(arr, open_, close + 1)
                arr.pop()
        ans = []
        backtrack([], 0, 0)
        return ans