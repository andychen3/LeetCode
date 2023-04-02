class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        def backtrack(curr, i):
            if len(curr) == len(digits):
                ans.append("".join(curr))
                return
            
            
            curr_digits = letters[digits[i]]
            for char in curr_digits:
                curr.append(char)
                backtrack(curr, i+1)
                curr.pop()
            
                  
        ans = []
        backtrack([], 0)
        return ans
        
