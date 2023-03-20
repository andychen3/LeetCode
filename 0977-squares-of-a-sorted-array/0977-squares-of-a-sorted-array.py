class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        
        left, right = 0, len(nums)-1
        
        for i in range(len(nums)-1, -1, -1):
            left_num = nums[left]**2
            right_num = nums[right]**2
            
            if left_num > right_num:
                ans[i] = left_num
                left += 1
            else:
                ans[i] = right_num
                right -= 1
        
        return ans
        
        