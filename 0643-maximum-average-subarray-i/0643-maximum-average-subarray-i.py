class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, ans, curr = 0, float('-inf'), 0
        
        for i in range(k):
            curr += nums[i]
        
        ans = curr / k

        for right in range(k, len(nums)):
            curr += nums[right]

            while right - left + 1 > k:
                curr -= nums[left]
                left += 1
            
            ans = max(curr / k, ans)
        
        return ans

        