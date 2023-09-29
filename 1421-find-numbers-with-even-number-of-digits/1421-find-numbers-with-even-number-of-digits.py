class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        string_num = [str(num) for num in nums]
        ans = 0

        for num in string_num:
            if len(num) % 2 == 0:
                ans += 1
        return ans