class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        for i in range(1, n+1):
            # i >> 1 is dividing by 2 and then adding i mod 2 which gives the significant bit
            dp[i] = dp[i >> 1] + (i & 1)
        return dp
            