class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0

        for banks in accounts:
            maximum = max(maximum, sum(banks))
        return maximum