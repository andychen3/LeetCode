class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        num_char = {'2': "abc", '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', 
                    '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        def backtrack(index, string):
            if index == len(digits):
                ans.append("".join(string[:]))
                return
            
            digit = num_char[digits[index]]
            for c in digit:
                string.append(c)
                backtrack(index + 1, string)
                string.pop()

        ans = []
        backtrack(0, [])
        return ans