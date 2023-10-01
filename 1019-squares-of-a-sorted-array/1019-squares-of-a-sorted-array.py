class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        left = 0
        right = i = len(nums) - 1
        

        while left <= right:
            left_num = nums[left] ** 2
            right_num = nums[right] ** 2
            if left_num >= right_num:
                ans[i] = left_num
                left += 1
            else:
                ans[i] = right_num
                right -= 1
            i -= 1
        return ans
        