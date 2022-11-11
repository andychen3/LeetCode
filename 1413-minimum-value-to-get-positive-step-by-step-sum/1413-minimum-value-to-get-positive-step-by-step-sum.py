class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        res = 1
        
        for i in range(1, len(nums)):
            nums[i] = nums[i-1]+nums[i]
            
        for num in nums:
            if num >= 1:
                continue
            else:
                res = max(res, abs(num-1))
                
        return res

            

        