class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0

        for index, num in enumerate(nums):
            if left_sum + num == right_sum - left_sum:
                return index
            
            left_sum += num
        
        return -1
        
