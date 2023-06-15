class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        
        for index, num in enumerate(nums):
            left = index + 1
            right = len(nums) - 1
            while left < right:
                total = num + nums[left] + nums[right]
                if abs(res - target) > abs(total - target):
                    res = total
                if total > target:
                    right -= 1
                else:
                    left += 1
        return res