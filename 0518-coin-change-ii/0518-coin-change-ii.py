class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (n+1) for _ in range(amount + 1)]

        for i in range(n+1):
            dp[0][i] = 1

        for remain in range(amount+1):
            for i in range(n -1, -1, -1):
                if remain - coins[i] >= 0:
                    dp[remain][i] = dp[remain - coins[i]][i] + dp[remain][i+1]
                else:
                    dp[remain][i] = dp[remain][i+1]
        
        print(dp)
        return dp[amount][0]
