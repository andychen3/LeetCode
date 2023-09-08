class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # # Reason why you do n + 1 instead of n because at the first choice
        # # if you skip you have 0. You don't automatically take the question
        # # because it affects future decisions. 
        # # This will prevent out of bounds
        n = len(questions)
        dp = [0] * n
        dp[-1] = questions[-1][0]

        for i in range(n - 2, -1, -1): # n - 1 To stay in bounds
            # how to skip a question?
            
            j = i + questions[i][1] + 1
            if j < n:
                dp[i] += dp[j]
            # To take or not take? And you want to maximize it
            # we do min because j could be out of bounds.
            dp[i] = max(dp[i + 1], questions[i][0] + dp[i])

        print(dp)
        return dp[0]