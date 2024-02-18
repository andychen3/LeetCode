class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        n = len(nums)
        curr_sum = total // 2
        dp = [[False] * (n + 1) for _ in range(curr_sum + 1)]
        dp[curr_sum][n] = True
        
        
        for remain in range(curr_sum - 1, -1, -1):
            for i in range(n - 1, -1, -1):
                dp[remain][i] = dp[remain][i+1]
                if remain + nums[i] <= curr_sum:
                    dp[remain][i] = dp[remain][i] or dp[remain + nums[i]][i+1]
        return dp[0][0]
        
        
#         total = sum(nums)
        
#         if total % 2 == 1:
#             return False
        
#         @cache
#         def dp(remain, i):
#             if remain == curr_sum:
#                 return True
#             if i == len(nums) or remain > curr_sum:
#                 return False
            
#             return dp(remain, i+1) or dp(remain + nums[i], i + 1)
#         curr_sum = total // 2                                
#         return dp(0, 0)
            