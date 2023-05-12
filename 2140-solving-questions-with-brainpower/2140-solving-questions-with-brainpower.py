class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dp(i):
            if i >= len(questions):
                return 0
            
            # or not skip
            not_skip = questions[i][1] + 1 + i
            
            return max(dp(i+1), dp(not_skip) + questions[i][0])
            
        return dp(0)