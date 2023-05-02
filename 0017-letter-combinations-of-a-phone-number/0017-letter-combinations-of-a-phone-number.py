class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hash_map = {'2':'abc', '3':'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9':'wxyz'}
        def backtrack(arr, i):
            if i >= len(digits):
                ans.append("".join(arr[:]))
                return

            
            mapping = hash_map[digits[i]]
            for char in mapping:
                arr.append(char)
                backtrack(arr, i+1)
                arr.pop()
            
        
        
        ans = []
        backtrack([], 0)
        return ans