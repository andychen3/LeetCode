class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        left, right = 0, len(nums) - 1
        idx = len(nums) - 1
        
        while left <= right:
            left_num = (nums[left])**2
            right_num = (nums[right])**2
            
            if left_num >= right_num:
                ans[idx] = left_num
                left += 1
            elif right_num > left_num:
                ans[idx] = right_num
                right -= 1
            idx -= 1
        return ans