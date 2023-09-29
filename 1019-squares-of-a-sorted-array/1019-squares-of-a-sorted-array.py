class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        left = 0
        right = idx = len(nums) - 1
        

        while left <= right:
            left_num = nums[left] ** 2
            right_num = nums[right] ** 2
            if left_num >= right_num:
                ans[idx] = left_num
                idx -= 1
                left += 1
            elif right_num > left_num:
                ans[idx] = right_num
                idx -= 1
                right -= 1
        return ans