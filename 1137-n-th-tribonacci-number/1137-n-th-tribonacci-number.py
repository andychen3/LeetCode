class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def dp(i):
            if i == 0:
                return 0
            if i <= 2:
                return 1
            return dp(i-3) + dp(i-2) + dp(i-1)
        return dp(n)