class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(arr, i, total):
            if len(arr) == k and total == n:
                ans.append(arr[:])
                return
            
            for j in range(i, 10):
                if total + j <= n:
                    arr.append(j)
                    backtrack(arr, j + 1, total + j)
                    arr.pop()
                
                
        ans = []
        backtrack([], 1, 0)
        return ans