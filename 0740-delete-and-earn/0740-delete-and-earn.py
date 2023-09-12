from collections import defaultdict
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_num = max(nums)
        for num in nums:
            points[num] += num
        
        dp = [0] * (max_num + 1)
        dp[1] = points[1]

        for i in range(2, max_num + 1):
            dp[i] = max(dp[i-1], dp[i-2] + points[i])
        
        return dp[max_num]
