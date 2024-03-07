class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(remaining):
            if remaining < 0:
                return inf
            if remaining == 0:
                return 0
            ans = inf
            
            for c in coins:
                ans = min(ans, dp(remaining - c) + 1)
            return ans
        return dp(amount) if dp(amount) != inf else -1