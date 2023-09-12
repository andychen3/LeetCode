from functools import cache
from collections import defaultdict
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_num = max(nums)
        for num in nums:
            points[num] += num
            
        @cache
        def dp(i):
            if i == 0:
                return 0

            if i == 1:
                return points[1]

            return max(dp(i-1), dp(i-2) + points[i])
        return dp(max_num)


            