class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(arr, i, ans):
            if i > len(arr):
                return
            
            res.append(ans[:])
            
            for j in range(i, len(arr)):
                ans.append(arr[j])
                backtrack(arr, j+1, ans)
                ans.pop()
        
        
        
        res = []
        backtrack(nums, 0, [])
        return res