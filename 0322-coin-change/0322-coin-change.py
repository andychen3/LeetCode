class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0 # Base case

        for coin in coins:
            for remain in range(coin, amount+1):
                dp[remain] = min(dp[remain], dp[remain - coin] + 1)
        print(dp)
        return dp[amount] if dp[amount] != float("inf") else -1
