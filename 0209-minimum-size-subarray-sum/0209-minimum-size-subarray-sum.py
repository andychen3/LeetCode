class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = len(nums) + 1
        left, curr_sum = 0, 0

        for right, num in enumerate(nums):
            curr_sum += num

            while curr_sum >= target:
                min_length = min(min_length, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        
        return min_length if min_length != len(nums) + 1 else 0
