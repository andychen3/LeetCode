from functools import cache
from collections import defaultdict
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # We have a points dictionary because if we take an element we might as well take all of it
        points = defaultdict(int)
        # We find the max_num so we can start at that number and build down from there
        max_num = max(nums)
        # We populate our hash map with the total points for duplicate numbers
        for num in nums:
            points[num] += num
            
        @cache
        def dp(i):
            # i == 0 because i of 0 is always 0
            if i == 0:
                return 0

            # If i is 1 then we always take whatever 1 is.
            # The reason why this works because defaultdict will automatically place the 1 key
            # if the original nums did not have a 1 and the value would be 0.
            if i == 1:
                return points[1]

            # This is our recurrence relationship because if we decide to not take a num that means
            # we must have came from the last number and so we can take the total points of that number
            # If we do take the present number that means we aren't allowed to take the previous number
            # So we must have taken the total points from i-2
            return max(dp(i-1), dp(i-2) + points[i])
        return dp(max_num)


            