class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [nums[0]]
        
        for index in range(1,len(nums)):
            res.append(res[-1]+nums[index])
        
        return res