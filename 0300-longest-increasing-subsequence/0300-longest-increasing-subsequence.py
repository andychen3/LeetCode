class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
#         @cache
#         def dp(i):
#             ans = 1
            
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     ans = max(ans, dp(j)+1)
#             return ans
#         return max((dp(i) for i in range(len(nums))))