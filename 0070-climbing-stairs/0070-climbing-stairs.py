from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        # This is the correct recursive definition the others are wrong even though they work
        @cache 
        def dp(i):
            # We could so the shorthand of i <= 2 return i but this is more explicit

            # The reason we don't do 0 is because our constraint is n >= 1. So we will never get 0
            # as a testcase.
            # This also makes sense since we don't get zero that means the number of ways to reach 1 step
            # is 1 and to reach 2 is 2. (1+1) and (2)
            if i == 1:
                return 1

            if i == 2:
                return 2
            
            return dp(i-1) + dp(i-2)
        return dp(n)