from functools import cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            # We have ans = 1 because all numbers have a length of 1 that can be added
            # to the subsequence
            ans = 1

            # We use j as the pointer to go back from [0, i) and compare to the value of nums[i]
            # We only try to find the max length if nums[j] is less than nums of i
            for j in range(i):
                if nums[i] > nums[j]:
                    # The recurrence relationship is either the current ans is the longest subsequence or
                    # we add 1 to the longest subsequence we have found thus far before i
                    ans = max(ans, dp(j) + 1)
            return ans

        # We find the max subsequence from the recucrsion call from iterating from i to n
        return max(dp(i) for i in range(len(nums)))