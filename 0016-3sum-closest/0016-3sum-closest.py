class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = inf
        
        for i, num in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = target - (num + nums[left] + nums[right])
                if total == 0:
                    return target
                
                if abs(total) < abs(diff):
                    diff = total
                
                if total > 0:
                    left += 1
                else:
                    right -= 1
        return target - diff
                