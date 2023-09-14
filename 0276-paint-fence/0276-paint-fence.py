from functools import cache
class Solution:
    def numWays(self, n: int, k: int) -> int:
        @cache
        # Return the number of ways
        def dp(i):
            # Base cases
            # If we have 1 post then there is k ways to paint it
            if i == 1:
                return k

            # If we have 2 posts then there are k * k ways to paint it
            if i == 2:
                return k * k

            # Recurrence relation is
            # You have two options.
            # 1. Paint the post the same color but with restriction on third post
            # 2. Paint the post a different color
            return (k-1) * (dp(i-1) + dp(i-2))

        return dp(n)