class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = n - 1
        
        while start < n - 1 and nums[start] <= nums[start + 1]:
            start += 1
            
        if start == n - 1:
            return 0
        
        while end > 0 and nums[end] >= nums[end - 1]:
            end -= 1
            
        windowMax = max(nums[start:end+1])
        windowMin = min(nums[start:end+1])
        
        while start > 0 and nums[start-1] > windowMin:
            start -= 1
        
        
        while end < n - 1 and nums[end+1] < windowMax:
            end += 1
        return end - start + 1