class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(remaining):
            if remaining == 0:
                return 0
            ans = float("inf")
            for c in coins:
                if remaining - c >= 0:
                    ans = min(ans, dp(remaining - c)+1)
                    
            return ans
        
        res = dp(amount) 
        return res if res != float("inf") else -1
            
            