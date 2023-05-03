class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(arr, i):
            if i == len(s):
                ans.append(arr[:])
                return
            
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if substring == substring[::-1]:
                    arr.append(substring)
                    backtrack(arr, j+1)
                    arr.pop()   
            
        ans = []
        backtrack([], 0)
        return ans