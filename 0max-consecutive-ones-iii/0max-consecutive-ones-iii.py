class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = 0
        window_start = 0
        num_zeros = 0
        
        for window_end in range(len(nums)):
            if nums[window_end] == 0:
                num_zeros += 1
            
            while num_zeros > k:
                if nums[window_start] == 0:
                    num_zeros -= 1
                window_start += 1
            
            max_length = max(max_length, window_end-window_start+1)
        
        return max_length
                
        