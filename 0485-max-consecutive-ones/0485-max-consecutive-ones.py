class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = 0
        ans = 0

        for num in nums:
            if num == 1:
                ones += 1
            if num == 0:
                ones = 0
            ans = max(ones, ans)
        return ans
