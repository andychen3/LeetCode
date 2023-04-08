class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_total = 0
        
        
        for index, val in enumerate(nums):
            total -= val
            if left_total == total:
                return index
            left_total += val
        return -1
            
            