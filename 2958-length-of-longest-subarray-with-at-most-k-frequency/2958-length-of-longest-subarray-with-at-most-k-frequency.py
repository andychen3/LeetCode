from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        hash_map = defaultdict(int)
        ans = left = 0
        
        for right, num in enumerate(nums):
            hash_map[num] += 1
            
            while hash_map[num] > k:
                hash_map[nums[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        return ans
        