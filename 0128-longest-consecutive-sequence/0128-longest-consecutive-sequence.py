class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        longest = 0
        
        for num in hash_set:
            if num - 1 not in hash_set:
                length = 1
                while (num + 1) in hash_set:
                    length += 1
                    num += 1
                longest = max(longest, length)
        return longest