class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # We set all the values to 1 because all numbers have a length of 1
        dp = [1] * n

        for i in range(n):
            # We iterate to the ith number because we are using j to iterate from the start to i.
            # This allows us to check if there are any numbers before i that are less than i
            for j in range(i):
                if nums[i] > nums[j]:
                    # We start building the answer by finding the max of the current ith number
                    # or we add the current ith number which is 1 to the subsequence we were able to build
                    # before i
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)