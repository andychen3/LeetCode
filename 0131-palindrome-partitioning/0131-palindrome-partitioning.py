class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(i, arr):
            if i == len(s):
                ans.append(arr[:])
                return
            
            for j in range(i, len(s)):
                cur = s[i:j+1]
                if cur == cur[::-1]:
                    arr.append(cur)
                    backtrack(j+1, arr)
                    arr.pop()
            
            
        ans = []
        backtrack(0, [])
        return ans