class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        if n == 2:
            return min(cost[0], cost[1])

        one_step = 0
        two_step = 0

        for i in range(2, n + 1):
            temp = one_step
            one_step = min(one_step + cost[i-1], two_step + cost[i-2])
            two_step = temp
        return one_step