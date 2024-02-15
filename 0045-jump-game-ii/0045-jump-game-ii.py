class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        right = 0
        left = 0
        
        while right < len(nums) - 1:
            longest = 0
            for i in range(left, right + 1):
                longest = max(longest, i + nums[i])
            left = right + 1
            right = longest
            ans += 1
        return ans