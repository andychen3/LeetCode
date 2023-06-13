class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        N = len(nums)
        
        for i, num in enumerate(nums):
            left = i + 1
            right = N - 1
            while left < right:
                curr_sum = num + nums[left] + nums[right]
                if abs(res - target) > abs(curr_sum - target):
                    res = curr_sum
                if curr_sum > target:
                    right -= 1
                else:
                    left += 1
        return res
            
        