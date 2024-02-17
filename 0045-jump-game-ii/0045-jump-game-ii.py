class Solution:
    def jump(self, nums: List[int]) -> int:
        left, right, ans = 0, 0, 0
        
        while right < len(nums) - 1:
            longest = 0
            for i in range(left, right+1):
                longest = max(longest, nums[i] + i)
            left = right + 1
            right = longest
            ans += 1
        return ans
                