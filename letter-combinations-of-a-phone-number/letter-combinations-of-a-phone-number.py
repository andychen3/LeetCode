class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_hash = {'2':['a','b','c'],
                      '3':['d','e','f'],
                      '4':['g','h','i'],
                      '5':['j','k','l'],
                      '6':['m','n','o'],
                      '7':['p','q','r','s'],
                      '8':['t','u','v'],
                      '9':['w','x','y','z']}
        
        def backtrack(curr, i):
            if len(curr) == len(digits):
                string = "".join(curr)
                ans.append(string)
                return

            for index in range(i, len(digits)):
                for letters in digit_hash[digits[index]]:
                    curr.append(letters)
                    backtrack(curr, i+1)
                    curr.pop()
                break
        
        ans = []
        backtrack([], 0)
        return ans
        
        