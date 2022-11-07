class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(arr, j, length, total):
            if length == k and total == n:
                return ans.append(arr[:])
            
            for i in range(j, 10):
                if i not in arr:
                    arr.append(i)
                    backtrack(arr, i+1, length+1, total+i)
                    arr.pop()
            
        ans = []
        backtrack([], 1, 0, 0)
        return ans