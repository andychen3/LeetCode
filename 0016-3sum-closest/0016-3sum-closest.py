class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        N = len(nums)
        
        for index, num in enumerate(nums):
            left = index + 1
            right = N - 1
            while left < right:
                _sum = num + nums[left] + nums[right]
                if abs(ans - target) > abs(_sum - target):
                    ans = _sum
                
                if _sum > target:
                    right -= 1
                else:
                    left += 1
        return ans