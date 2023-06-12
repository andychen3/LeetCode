class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        size = len(nums)
        
        for index, num in enumerate(nums):
            left = index + 1
            right = size - 1
            while left < right:
                curr_sum = num + nums[left] + nums[right]
                if curr_sum < target:
                    res += right - left
                    left += 1
                else:
                    right -= 1
        return res