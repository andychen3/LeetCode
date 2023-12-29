from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash_map = defaultdict(int)
        ans = 0
        
        for num in nums:
            ans += hash_map[num]
            hash_map[num] += 1
        return ans
            