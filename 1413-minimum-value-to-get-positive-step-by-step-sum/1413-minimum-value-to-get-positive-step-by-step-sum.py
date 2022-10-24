class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        
        for index in range(1, len(nums)):
            prefix.append(prefix[-1]+nums[index])
        
        min_val = min(prefix)
        
        return abs(min_val) + 1 if min_val <= 0 else 1
            

        