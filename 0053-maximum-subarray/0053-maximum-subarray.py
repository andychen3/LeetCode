class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = float("-inf") 
        curr = 0
        for num in nums:
            curr = max(curr + num, num)
            total = max(total, curr)
        return total