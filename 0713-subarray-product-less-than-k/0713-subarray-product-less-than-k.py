class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        ans = left = 0
        total = 1
        
        for right, num in enumerate(nums):
            total *= num
            
            while total >= k:
                total //= nums[left]
                left += 1
            
            ans += right - left + 1
        return ans
        