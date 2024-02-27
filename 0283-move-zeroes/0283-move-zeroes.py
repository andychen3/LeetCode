class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        
        for i, num in enumerate(nums):
            if num != 0:
                nums[i], nums[zeros] = nums[zeros], nums[i]
                zeros += 1
        return nums