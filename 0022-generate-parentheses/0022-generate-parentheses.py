class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(arr, opening, closing):
            if opening + closing == 2 * n:
                ans.append("".join(arr[:]))
                return
            
            if opening < n:
                arr.append("(")
                backtrack(arr, opening + 1, closing)
                arr.pop()
            
            if closing < opening:
                arr.append(")")
                backtrack(arr, opening, closing + 1)
                arr.pop()
        ans = []
        backtrack([], 0, 0)
        return ans