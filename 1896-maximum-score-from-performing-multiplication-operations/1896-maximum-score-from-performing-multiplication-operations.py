from functools import cache
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @cache
        def dp(i, left):
            if i == m:
                return 0
            
            mult = multipliers[i]
            right = (n-1) - (i - left)
            return max(mult * nums[left] + dp(i+1, left+1), mult * nums[right] + dp(i+1, left))

        n = len(nums)
        m = len(multipliers)
        return dp(0, 0)