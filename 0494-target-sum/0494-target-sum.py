class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dp(i, total):
            if i >= len(nums) and total == target:
                return 1
            if i >= len(nums):
                return 0
            
            return dp(i+1, nums[i] + total) + dp(i+1, total - nums[i] )
        return dp(0,0)