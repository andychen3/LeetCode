class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            ans = 1
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    ans = max(ans, dp(j) + 1)
            return ans
        
        return max(dp(i) for i in range(len(nums)))