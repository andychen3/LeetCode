class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # We do len(nums) and not len(nums)+1 because we don't start with needing a subproblem of zero
        # At our first decision we can choose to rob the first house or not if there are only 1 house
        dp = [0] * len(nums)
        dp[0] = nums[0] # Base cases that are similar to top down. Here 0 represents the first house
        dp[1] = max(nums[0], nums[1])

        # We start at 2 because our base cases ended at 1.
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1] # Answer is at the end. We could also do len(nums)-1
