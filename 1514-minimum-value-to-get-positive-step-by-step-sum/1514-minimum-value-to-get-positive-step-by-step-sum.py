class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        min_val = nums[0]
        
        for i in range(1, len(nums)):
            curr_sum += nums[i]
            min_val = min(min_val, curr_sum)
        
        return -min_val + 1 if min_val < 1 else 1