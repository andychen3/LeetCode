class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        
        while i < len(nums):
            if nums[i] != i + 1:
                j = nums[i] - 1
                if nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    i += 1
            else:
                i += 1
        
        for i in range(len(nums)):
            if i+1 != nums[i]:
                ans.append(nums[i])
        
        return ans