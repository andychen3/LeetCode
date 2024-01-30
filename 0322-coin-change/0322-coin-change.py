class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(remaining):
            if remaining < 0:
                return float("inf")
            if remaining == 0:
                return 0
            
            ans = float("inf")
            
            for c in coins:
                ans = min(ans, dp(remaining - c) + 1)
            return ans
        return dp(amount) if dp(amount) != float("inf") else -1
            
            