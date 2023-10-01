class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        strings = [str(num) for num in nums]

        for num in strings:
            if len(num) % 2 == 0:
                ans += 1
        return ans
        