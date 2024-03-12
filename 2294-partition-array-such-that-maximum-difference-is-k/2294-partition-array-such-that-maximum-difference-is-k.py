class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        x = nums[0]
        
        for num in nums[1:]:
            if num - x > k:
                x = num
                ans += 1
        return ans