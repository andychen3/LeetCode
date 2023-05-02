class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(arr, i):
            if i > len(nums):
                return
            ans.append(arr[:])
            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                arr.append(nums[j])
                backtrack(arr, j+1)
                arr.pop()
        nums.sort()
        ans = []
        backtrack([], 0)
        return ans