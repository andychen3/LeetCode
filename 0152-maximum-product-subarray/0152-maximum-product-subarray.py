class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_val = 1
        max_val = 1
        ans = nums[0]
        
        for num in nums:
            temp = max(num, min_val * num, max_val * num)
            min_val = min(num, min_val * num, max_val * num)
            max_val = temp
            ans = max(max_val, ans)
        return ans