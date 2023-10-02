class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float("inf")
        left = 0
        curr = 0

        for right in range(len(nums)):
            curr += nums[right]

            while curr >= target:
                ans = min(ans, right - left + 1)
                curr -= nums[left]
                left += 1
        
        return ans if ans != float("inf") else 0
