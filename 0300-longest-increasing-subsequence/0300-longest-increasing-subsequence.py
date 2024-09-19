class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(i):
            if i > n:
                return 0
            
            ans = 1

            for j in range(i, n):
                if nums[j] > nums[i]:
                    ans = max(ans, dp(j)+1)
            
            return ans

        return max(dp(index) for index in range(n))