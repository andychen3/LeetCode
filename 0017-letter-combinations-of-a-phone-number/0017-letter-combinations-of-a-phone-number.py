class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        numbers = {"2": "abc", "3": "def", "4": "ghi",
                        "5": "jkl", "6": "mno", "7": "pqrs", 
                         "8": "tuv", "9": "wxyz"}
        
        def backtrack(arr, i):
            if len(arr) == len(digits):
                ans.append("".join(arr[:]))
                return
            
            curr = numbers[digits[i]]
            for num in curr:
                arr.append(num)
                backtrack(arr, i + 1)
                arr.pop()
                
            
        ans = []
        backtrack([], 0)
        return ans