class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0

        strings = [str(num) for num in nums]

        for string in strings:
            if len(string) % 2 == 0:
                ans += 1
        return ans