class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def two_ptrs(left, right, third):
            while left < right:
                ans = nums[left] + nums[right] + third
                if ans == 0:
                    res.append([nums[left], nums[right], third])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif ans > 0:
                    right -= 1
                else:
                    left += 1
        
        res = []
        right = len(nums)-1
        
        for index, num in enumerate(nums):
            if index > 0 and num == nums[index-1]:    
                continue
            two_ptrs(index+1, right, num)
        return res
        
        
        
        
                    