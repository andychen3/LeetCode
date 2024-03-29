class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[n - 1]
#         @cache
#         def dp(i):
#             if i == 0:
#                 return nums[i]
#             if i == 1:
#                 return max(nums[0], nums[1])
            
#             return max(nums[i] + dp(i-2), dp(i-1))
#         return dp(len(nums) - 1)