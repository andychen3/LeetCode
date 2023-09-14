from functools import cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            # When you reach the end of the nums array
            if i == len(nums):
                return 0

            # Because every number itself can be a subsequence
            ans = 1
            # We iterate through nums starting at i because we can't reuse the same number
            for j in range(i, len(nums)):
                # If j which are all numbers that come after i. if any are greater tahn nums[i]
                # that means a potnetial subsequence can be formed
                if nums[j] > nums[i]:
                    # We want the max of that and then we recurse on j. We also add 1 because that means
                    # we extended the subsequence
                    ans = max(ans, dp(j) + 1)
            return ans

        # We iterate through the whole length of nums and find the max subsequence that was formed
        return max([dp(i) for i in range(len(nums))])