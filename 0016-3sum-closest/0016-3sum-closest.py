class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = inf
        
        for i, num in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            while left < right:
                target_diff = target - (num + nums[left] + nums[right])
                if target_diff == 0:
                    return target
                
                if abs(target_diff) < abs(diff):
                    diff = target_diff
                    
                if target_diff > 0:
                    left += 1
                else:
                    right -= 1
        return target - diff