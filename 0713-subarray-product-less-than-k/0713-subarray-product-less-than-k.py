class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        res = 0
        left = 0
        running_product = 1
        
        for right, num in enumerate(nums):
            running_product *= nums[right]
                
            while running_product >= k:
                running_product /= nums[left]
                left += 1
            res += right - left + 1
        
        return res
            