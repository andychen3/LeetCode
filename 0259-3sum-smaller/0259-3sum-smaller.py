class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        size = len(nums)
        
        for index, num in enumerate(nums):
            left = index + 1
            right = size - 1
            while left < right:
                total = num + nums[left] + nums[right]
                if total < target:
                    res += right - left
                    
                if total >= target:
                    right -= 1
                else:
                    left += 1
                
                    
        return res