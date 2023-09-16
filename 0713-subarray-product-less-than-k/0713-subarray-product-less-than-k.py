class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # We have k <= 1 and not k <= 1 because we start our curr at 1
        # Any answer in nums will exceed k if k == 1. Thus we have to have a condition to return 0
        if k <= 1:
            return 0

        left = ans = 0
        curr = 1

        for right, num in enumerate(nums):
            curr *= num

            while curr >= k:
                curr //= nums[left]
                left += 1
            
            ans += right - left + 1
        return ans