class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def backtrack(arr, index):
            if index > len(nums):
                return
            ans.append(arr[:])
        
        
            for i in range(index, len(nums)):
                num = nums[i]
                if i != index and nums[i - 1] == nums[i]:
                    continue
                arr.append(num)
                backtrack(arr, i + 1)
                arr.pop()
        
        ans = []
        backtrack([], 0)
        return ans