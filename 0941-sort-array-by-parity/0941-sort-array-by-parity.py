class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ptr = 0
        n = len(nums)
        for i in range(n):
            # We are looking for the even number to switch with ptr.
            # We don't care if ptr is an even or odd number because if its even everytime we switch it
            # with another even we move ptr up until we find an odd number
            if nums[i] % 2 == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        return nums
        