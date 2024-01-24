class Solution:
    def rob(self, nums: List[int]) -> int:
        # What is the function trying to return and waht arg can i use?
        # max amount of money. 1d array so probably i will work
        # What is the recurrence relation?
        # 1 house or 2nd house. Max of them both
        # What are the base cases?
        # i = 0 then pick the house that has the most
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        
        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        return dp[n-1]
        
        
#         @cache
#         def dp(i):
#             if i == 0:
#                 return nums[0]
#             if i == 1:
#                 return max(nums[0], nums[1])
            
#             return max(nums[i] + dp(i-2), dp(i-1))
        
#         return dp(len(nums) - 1)
