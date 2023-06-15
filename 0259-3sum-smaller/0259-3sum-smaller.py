class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        
        for index, num in enumerate(nums):
            left = index + 1
            right = len(nums) - 1
            while left < right:
                total = num + nums[left] + nums[right]
                if total < target:
                    res += right - left
                    left += 1
                else:
                    right -= 1
        return res