class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        
        while i < len(nums):
            correct_idx = nums[i] - 1
            if nums[i] != nums[correct_idx]:
                    nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1
        
        for i in range(len(nums)):
            if i+1 != nums[i]:
                ans.append(nums[i])
        
        return ans