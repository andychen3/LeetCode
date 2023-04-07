class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        longest = 0
        
        for num in nums:
            if num - 1 not in hash_set:
                length = 1
                while num + 1 in hash_set:
                    num += 1
                    length += 1
                longest = max(longest, length)
                
        return longest