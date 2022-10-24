class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        length = len(nums)
        max_sum = sum(nums[:k])
        temp_sum = max_sum
        
        for index in range(length-k):
            temp_sum -= nums[index]
            temp_sum += nums[k+index]
            if max_sum < temp_sum:
                max_sum = temp_sum
        return max_sum/k
        
        
#         max_average = float(-inf)
#         window_start = 0
#         total = 0
        
#         for window_end in range(len(nums)):
#             total += nums[window_end]
        
#             while window_end-window_start+1 > k:
#                 total -= nums[window_start]
#                 window_start += 1
            
#             if window_end-window_start + 1 == k:
#                 max_average = max(max_average, total/k)
            
#         return max_average