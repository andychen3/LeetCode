class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0 # 0 coins to make 0 value

        # We should start from iterating through the coins list because we can only use those coins
        # instead of starting from iterating through the range of 1 to amount + 1 inclusive.
        # This saves unnecessary iterations.
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        
        return dp[amount] if dp[amount] != float("inf") else -1