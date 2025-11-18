class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, ans, curr = 0, float('-inf'), 0
        
        for right, num in enumerate(nums):
            curr += num
            
            while right - left + 1 >= k:
                ans = max(curr / k, ans)
                curr -= nums[left]
                left += 1
            
            
        
        return ans