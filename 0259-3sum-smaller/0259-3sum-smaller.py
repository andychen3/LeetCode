class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        
        nums.sort()
        res = 0
        
        for index, num in enumerate(nums):
            left = index + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = num + nums[left] + nums[right]
                if curr_sum < target:
                    res += right - left
                    left += 1
                else:
                    right -= 1
        return res
        
        
        
        