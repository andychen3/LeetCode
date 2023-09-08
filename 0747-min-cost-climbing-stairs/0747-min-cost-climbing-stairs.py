class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1) # n + 1 because the answer is built from previous two.
        dp[2] = cost[0]

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i-1], dp[i-2] + cost[i-2])
        print(dp)
        return dp[n]
