class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        right_total = 0
        res = 0

        for i in range(len(nums) - 1):
            right_total += nums[i]
            total -= nums[i]
            if (right_total - total) % 2 == 0:
                res += 1
            
        
        return res