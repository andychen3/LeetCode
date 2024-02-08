class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        num_to_letter = {"2": "abc", "3": "def", "4": "ghi",
                        "5": "jkl", "6": "mno", "7": "pqrs", 
                         "8": "tuv", "9": "wxyz"}
        def backtrack(string, index):
            if index == len(digits):
                ans.append("".join(string))
                return
            
            letters = num_to_letter[digits[index]]
            for char in letters:
                string.append(char)
                backtrack(string, index + 1)
                string.pop()
            
            
            
        ans = []
        backtrack([], 0)
        return ans
        