class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        ans = 0
        
        for num in nums:
            if num - 1 not in hash_set:
                longest = 1
                while num + longest in hash_set:
                    longest += 1
                ans = max(ans, longest)
        return ans