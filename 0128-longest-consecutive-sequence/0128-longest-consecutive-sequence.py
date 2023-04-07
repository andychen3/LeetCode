class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        hash_set = set(nums)
        
        for n in nums:
            if n-1 not in hash_set:
                streak = 1
                while n+1 in hash_set:
                    n+= 1
                    streak += 1
                longest = max(longest, streak)
        return longest
                