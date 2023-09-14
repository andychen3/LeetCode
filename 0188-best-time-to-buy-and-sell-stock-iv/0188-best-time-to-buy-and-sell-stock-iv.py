class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0] * (k+1) for _ in range(2)] for _ in range(n+1)]

        for i in range(n - 1, -1, -1):
            for holding in range(2):
                for remaining in range(1, k + 1): # We skip 0 because that is a base case 
                    skip = dp[i+1][holding][remaining]
                    ans = 0

                    if holding:
                        ans = prices[i] + dp[i+1][0][remaining - 1]
                    else:
                        ans = -prices[i] + dp[i+1][1][remaining]
                    
                    dp[i][holding][remaining] = max(ans, skip)
        
        return dp[0][0][k]





        @cache
        def dp(i, remaining, holding):
            if i == len(prices) or remaining == 0:
                return 0

            # do nothing
            skip = dp(i+1, remaining, holding)
            ans = 0
            #recurrence relation
            # I can buy, sell, or do nothing
            if holding: # We have a stock
                ans = prices[i] + dp(i+1, remaining - 1, 0)
            else:
                ans = -prices[i] + dp(i+1, remaining, 1)
            
            return max(ans, skip)

        return dp(0, 0, k)