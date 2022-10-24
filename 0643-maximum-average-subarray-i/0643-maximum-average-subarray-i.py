class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_average = float(-inf)
        window_start = 0
        total = 0
        
        for window_end in range(len(nums)):
            total += nums[window_end]
        
            while window_end-window_start+1 > k:
                total -= nums[window_start]
                window_start += 1
            
            if window_end-window_start + 1 == k:
                max_average = max(max_average, total/k)
            
        return max_average