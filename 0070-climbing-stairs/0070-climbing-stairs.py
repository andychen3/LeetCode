from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        # this is a dp problem only because i have seen it. and it is asking how many distinct ways
        # So there are overlapping subproblems
        @cache
        def dp(i):
            if i == 0:
                return 1

            if i == 1:
                return 1
            
            return dp(i-1) + dp(i-2)
        return dp(n)