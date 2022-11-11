class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        
        for index, num in enumerate(nums):
            if left == (right-left-num):
                return index
            left += num
        
        return -1
            