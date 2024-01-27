class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = len(nums)
        
        for i, num in enumerate(nums):
            ans ^= num ^ i
        return ans