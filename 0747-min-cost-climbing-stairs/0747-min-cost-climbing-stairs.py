from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dp(i):
            # Because we can start at the 0th or 1st index. The initial starting cost is 0
            if i == 0:
                return 0

            if i == 1:
                return 0

            return min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])
        return dp(len(cost))