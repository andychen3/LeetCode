class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        ans = 1

        for right, num in enumerate(nums):
            if num - nums[left] <= k:
                continue
            
            ans += 1

            while num - nums[left] > k:
                left = right 
        
        return ans

        