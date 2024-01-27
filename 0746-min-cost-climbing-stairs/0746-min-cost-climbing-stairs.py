class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dp(i):
            if i <= 1:
                return 0
            
            return min(cost[i-2] + dp(i - 2), cost[i - 1] + dp(i - 1))
        return dp(len(cost))