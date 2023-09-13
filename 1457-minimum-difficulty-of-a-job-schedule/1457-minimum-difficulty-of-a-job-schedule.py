class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        dp = [[float("inf")] * (d+1) for _ in range(n)]

        # We set this as a base case because we always have to do 1 task per day
        # So on the last day the difficulty is the last job 
        dp[-1][d] = jobDifficulty[-1]

        # We do n-2 because we skip the last element since we already declared it with
        # the base case. and we do n-1 normally because of 0 indexed array
        for i in range(n-2, -1,-1):
            # We want the max because if we can only split in the example we do 1 job and then the rest of
            # the days are done on the last day. We want the max difficulty per day
            dp[i][d] = max(dp[i+1][d], jobDifficulty[i])

        for day in range(d-1, 0, -1): # We start iterating from the second to last day
            # We start iterating from whatever day is to the jobs before the end of day.
            # we do day - 1 because in the example there are 10 jobs. and 6 days.
            # We know that day from the first for loop would be 5. We start i at 4 because 
            # the first 4 jobs 0,1,2,3 have to be in day 1 in order for there to be enough jobs to fit 6 days.
            # And n - (d - day) will be 10 - (6 -5) = 9. Because we reservere the last job for the last day.
            # So everything in between 4-9 if divided 1 job per day so 0-4, 5, 6, 7, 8, (last 9) can be indiviudal jobs this equals 6 total days.
            for i in range(day - 1, n - (d - day)):
                hardest = 0
                # iterate over the options and choose the best
                # We put i here because we can only start on the ith job in order to allow for fitting all
                # the jobs in the amount of days asked if each day has to do one job
                for j in range(i, n - (d - day)):
                    hardest = max(hardest, jobDifficulty[j])
                    # Recurrence relation
                    dp[i][day] = min(dp[i][day], hardest + dp[j+1][day+1])

        return dp[0][1]