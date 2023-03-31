class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        left = 0
        
        for index, val in enumerate(nums):
            if val - nums[left] > k:
                ans += 1
                left = index
        return ans