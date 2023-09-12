from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            # Because of 0 indexing. This is if we are at the first house
            # We rob it if this is the only house.
            if i == 0:
                return nums[0]
            
            # This is if we have two houses
            if i == 1:
                return max(nums[0], nums[1])
            
            return max(dp(i-1), dp(i-2) + nums[i])
        
        return dp(len(nums) - 1)
