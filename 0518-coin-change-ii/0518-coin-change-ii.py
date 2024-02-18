class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dp(i, remaining):
            if i == len(coins):
                return 0
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0
            
            return dp(i + 1, remaining) + dp(i, remaining - coins[i])
            
        return dp(0, amount)