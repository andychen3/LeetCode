class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        curr_sum = 0
        min_val = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            min_val = min(min_val, curr_sum)
        
        return -min_val+1 if min_val <= 0 else 1