class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        total = nums[0]
        
        for num in nums[1:]:
            if num - total > k:
                total = num
                ans += 1
        return ans