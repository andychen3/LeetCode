class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd_nums = 0
        n = len(nums)
        for i in range(n):
            if nums[i] % 2 != 0:
                odd_nums = i
                break
        
        for i in range(odd_nums, n):
            if nums[i] % 2 == 0:
                nums[odd_nums], nums[i] = nums[i], nums[odd_nums]
                odd_nums += 1
        return nums