class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(i, arr):
            if len(arr) == k:
                ans.append(arr[:])
                return
            
            for num in range(i, n + 1):
                arr.append(num)
                backtrack(num + 1, arr)
                arr.pop()
        ans = []
        backtrack(1, [])
        return ans