class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        
        for index, val in enumerate(nums):
            if index > 0 and nums[index-1] == val:
                continue
            left = index + 1
            right = len(nums)-1
            while left < right:
                total = val + nums[left] + nums[right]
                if total == 0:
                    res.append([val, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1 
                if total < 0:
                    left += 1
                else:
                    right -= 1
        return res
        
        