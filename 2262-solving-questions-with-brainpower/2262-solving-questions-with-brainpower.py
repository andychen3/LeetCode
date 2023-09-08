class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        # If you don't do n + 1 then you have to set the last index to the last points in
        # questions
        dp[-1] = questions[-1][0]

        for i in range(n - 2, -1, -1): # n - 2 To stay in bounds we start from 2 index
            # how to skip a question?
            j = i + questions[i][1] + 1
            # add the value of skip if j is in bounds of array
            if j < n:
                dp[i] += dp[j]
            # To take or not take? And you want to maximize it
            dp[i] = max(dp[i + 1], questions[i][0] + dp[i])

        return dp[0]