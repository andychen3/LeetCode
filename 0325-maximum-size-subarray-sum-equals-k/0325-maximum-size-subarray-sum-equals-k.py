class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix = 0
        longest = 0
        hash_map = {}
        
        for index, num in enumerate(nums):
            prefix += num
            
            if prefix == k:
                longest = index + 1
                
            if prefix - k in hash_map:
                longest = max(longest, index - hash_map[prefix - k])
            
            if prefix not in hash_map:
                hash_map[prefix] = index
        return longest