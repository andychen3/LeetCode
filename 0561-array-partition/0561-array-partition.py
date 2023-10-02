class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        i = 0


        while i < len(nums):
            ans += min(nums[i], nums[i+1])
            i += 2
        return ans
