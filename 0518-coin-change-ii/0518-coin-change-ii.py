class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dp(remain, i):
            if i >= len(coins) or remain < 0:
                return 0
            
            if remain == 0:
                return 1
            
            return dp(remain - coins[i], i) + dp(remain, i + 1)
        return dp(amount, 0)