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
            # J represents all elements before i. so that means in order to increase we j have to be
            # less than i.
            for j in range(i):
                if nums[j] < nums[i]:
                    # We want the max of that and then we recurse on j. We also add 1 because that means
                    # we extended the subsequence
                    ans = max(ans, dp(j) + 1)
            return ans

        # We iterate through the whole length of nums and find the max subsequence that was formed
        return max([dp(i) for i in range(len(nums))])