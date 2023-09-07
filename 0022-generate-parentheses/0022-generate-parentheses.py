class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(i, left_count, right_count, arr):
            # We have 2 * n because we want a combination of "(" and ")" so there is 2n.
            if i == 2 * n:
                # We have to join the parantheses into one string
                ans.append("".join(arr[:])) 
                return
            
            # Check for valid opening parentheses up until n
            if left_count < n:
                arr.append("(")
                backtrack(i + 1, left_count + 1, right_count, arr)
                arr.pop()
            
            # Add closing parantheses only up to the amount of opening parantheses else
            # it won't be valid
            if right_count < left_count:
                arr.append(")")
                backtrack(i + 1, left_count, right_count + 1, arr)
                arr.pop()
            
        ans = []
        
        backtrack(0, 0, 0, [])
        return ans