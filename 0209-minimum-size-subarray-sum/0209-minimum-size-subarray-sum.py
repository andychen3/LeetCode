class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = len(nums)+1
        left = 0
        total = 0
        
        for right, num in enumerate(nums):
            total += num
            
            while total >= target:
                min_length = min(right - left + 1, min_length)
                total -= nums[left]
                left += 1
        
        return min_length if min_length != len(nums) + 1 else 0