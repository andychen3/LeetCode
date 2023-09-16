class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        
        min_val = min(prefix)

        return -min_val+1 if min_val <= 0 else 1 