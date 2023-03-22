class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int: 
        min_length = len(nums) + 1
        left = 0
        total = 0
        
        for right in range(len(nums)):
            total += nums[right]
            
            while total >= target:
                min_length = min(min_length, right - left + 1)
                total -= nums[left]
                left += 1
                
        return min_length if min_length <= len(nums) else 0
                
        