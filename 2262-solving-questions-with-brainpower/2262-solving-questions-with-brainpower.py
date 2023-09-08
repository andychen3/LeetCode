from functools import cache
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dp(i):
            # This is the base case because if the length is greater than the array then there is
            # no more questions to solve
            if i >= len(questions):
                return 0

            # How to skip a question?
            j = i + questions[i][1] + 1

            # Why is it dp of j? It is dp of j because j represents the next question you can solve
            # after you skip brainpower. Also, if you solve a question you get x points
            return max(questions[i][0] + dp(j), dp(i + 1))
        
        # Why do you iterate from 0? Because you are starting from the beginning.
        return dp(0)