class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            # We are declaring that j is all elements before i. i is what we are using to iterate through
            # the array. So that means in order to form an increasing sub we have to have j be all elements before i that are less than i.
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
