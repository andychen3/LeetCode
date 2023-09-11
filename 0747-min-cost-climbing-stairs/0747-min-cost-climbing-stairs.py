class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1) # Reason is because we start at 0 and 1 index and they are zero

        for i in range(2, n + 1): # We start from 2 because we can start at 0 and 1 and its 0
            dp[i] = min(dp[i - 1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[n]