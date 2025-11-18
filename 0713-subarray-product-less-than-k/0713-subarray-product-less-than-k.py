class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        left, product = 0, 1
        ans = 0

        for right, num in enumerate(nums):
            product *= num

            while left < len(nums) and product >= k:
                product //= nums[left]
                left += 1
            
            ans += right - left + 1
        
        return ans
