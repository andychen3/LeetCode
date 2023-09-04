class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        ans = 1

        for right, num in enumerate(nums):
            if num - nums[left] > k:
                ans += 1    
                left = right 
        
        return ans

        