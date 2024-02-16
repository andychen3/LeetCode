class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(arr, index):
            if len(arr) > len(nums):
                return
            
            ans.append(arr[:])
        
            for i in range(index, len(nums)):
                arr.append(nums[i])
                backtrack(arr, i + 1)
                arr.pop()
                
        
        ans = []
        backtrack([], 0)
        return ans