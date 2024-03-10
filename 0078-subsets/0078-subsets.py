class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(arr, i):
            if i > len(nums):
                return
            ans.append(arr[:])
            
            for j in range(i, len(nums)):
                arr.append(nums[j])
                backtrack(arr, j + 1)
                arr.pop()
        ans = []
        backtrack([], 0)
        return ans