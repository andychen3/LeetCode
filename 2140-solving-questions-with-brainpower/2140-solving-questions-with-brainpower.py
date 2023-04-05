class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dp(i):
            if i >= len(questions):
                return 0
            
            j = i + questions[i][1] + 1
            
            return max(dp(i+1), questions[i][0] + dp(j))
        
        return dp(0)