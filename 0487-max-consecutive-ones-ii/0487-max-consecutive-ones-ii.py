class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        zeros = 1
        left = 0
        ans = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros -= 1

            while zeros < 0:
                if nums[left] == 0:
                    zeros += 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans