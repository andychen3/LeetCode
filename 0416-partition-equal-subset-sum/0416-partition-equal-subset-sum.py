class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 == 1:
            return False
        
        @cache
        def dp(remain, i):
            if remain == curr_sum:
                return True
            if i == len(nums) or remain > curr_sum:
                return False
            
            return dp(remain, i+1) or dp(remain + nums[i], i + 1)
        curr_sum = total // 2                                
        return dp(0, 0)
            