class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        left_total = 0
        
        
        for index, val in enumerate(nums):
            total -= val
            if left_total == total:
                return index
            left += 1
            left_total += val
        return -1
            
            