class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_sub = 1
        window_start = 0
        
        for window_end in range(1, len(nums)):
            if nums[window_end] <= nums[window_end-1]:
                window_start = window_end
                
            max_sub = max(max_sub, window_end-window_start+1)
        
        return max_sub