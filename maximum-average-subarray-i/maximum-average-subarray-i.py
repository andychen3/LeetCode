class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0
        
        for i in range(k):
            curr += nums[i]
            
        ans = curr / k
        
        for j in range(k, len(nums)):
            curr += nums[j] - nums[j - k]
            ans = max(ans, curr / k)
        
        return ans
            