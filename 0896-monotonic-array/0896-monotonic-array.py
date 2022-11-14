class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True
        
        for index in range(1, len(nums)):
            if nums[index-1] > nums[index]:
                increasing = False
            if nums[index-1] < nums[index]:
                decreasing = False
                
                
        return increasing or decreasing
        