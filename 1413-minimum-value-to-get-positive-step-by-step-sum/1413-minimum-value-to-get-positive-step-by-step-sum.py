class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val = nums[0]
        total = nums[0]
        
        for index in range(1,len(nums)):
            total += nums[index]
            min_val = min(min_val, total)
            
        return -min_val+1 if min_val <= 0 else 1
        
#         prefix = [nums[0]]
        
#         for index in range(1, len(nums)):
#             prefix.append(prefix[-1]+nums[index])
        
#         min_val = min(prefix)
        
#         return abs(min_val) + 1 if min_val <= 0 else 1
            

        