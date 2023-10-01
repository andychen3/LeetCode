class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        distinct = 0

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                distinct += 1
            if distinct == 3:
                return nums[i]
        
        return nums[0]
        

