class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find the first zero
        zero_ptr = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_ptr = i
                break
        # Start the next iteration from where the zero_ptr is + 1 and switch
        # if num[zero_ptr] is a zero and nums[i] is not
        for i in range(zero_ptr+1, len(nums)):
            if nums[zero_ptr] == 0 and nums[i] != 0:
                nums[i], nums[zero_ptr] = nums[zero_ptr], nums[i]
                zero_ptr += 1
        return nums

