class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_ptr = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                zero_ptr = i
                break
        
        for ptr in range(zero_ptr, n):
            if nums[ptr] != 0:
                nums[zero_ptr], nums[ptr] = nums[ptr], nums[zero_ptr]
                zero_ptr += 1
        return nums