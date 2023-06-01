class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        left, right = 0, len(nums)-1
        index = len(nums) - 1
        
        while left <= right:
            left_num = nums[left]**2
            right_num = nums[right]**2
            
            if left_num <= right_num:
                ans[index] = right_num
                right -= 1
            else:
                ans[index] = left_num
                left += 1
            index -= 1
        return ans
                
        