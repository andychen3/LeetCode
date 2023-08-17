class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        min_length = len(nums)
        left, curr_sum = 0, 0

        for right, num in enumerate(nums):
            curr_sum += num

            while curr_sum >= target:
                min_length = min(min_length, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        
        return min_length 
