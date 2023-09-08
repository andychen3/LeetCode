from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dp(i):
            if i == 0:
                return 0
            if i == 1:
                return 0

            # Recurrence relationship
            # Min of taking one step and two steps.
            # When you take either step you incur the cost of that step
            return min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])
        return dp(len(cost))