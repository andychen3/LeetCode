from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(i):
            # The previous solutions are wrong with i == 0 == 0.
            # i == 0 = 1 because we have to account for when n == 2. So if 
            # dp(i-2) represents taking 2 steps. When n == 2. It should equal 1. 
            # if i == 0 = 0, that wouldn't make sense because if n == 2 and you take 2 steps. it will 
            # be one distinct way to get there not 0.

            # in order to figure out base cases you start with recurrence relation and then figure out
            # what is true. The thing that threw me off was starting from the bottom which is 0 step.
            # but that was something i created. It wasn't said in the problem. It just asked you how many
            # distinct ways to reach to the top if given n steps and that you are allowed to take 1 or 2
            if i == 0:
                return 1
            
            if i == 1:
                return 1
            

            return dp(i - 1) + dp(i - 2)
        return dp(n)