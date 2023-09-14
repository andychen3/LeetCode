class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n+2)]

        for i in range(n - 1, -1 ,-1):
            for holding in range(2):
                skip = dp[i+1][holding]

                if holding:
                    do_something = prices[i] + dp[i+2][0]
                else:
                    do_something = -prices[i] + dp[i+1][1]
                
                dp[i][holding] = max(skip, do_something)
        print(dp)
        return dp[0][0]
