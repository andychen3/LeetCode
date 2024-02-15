class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dp(i, total):
            if i == len(nums) and total == target:
                return 1
            
            if i >= len(nums):
                return 0
            
            ways = 0
            
            ways += dp(i+1, total + nums[i]) + dp(i + 1, total - nums[i])
            
            return ways
        
        return dp(0,0)