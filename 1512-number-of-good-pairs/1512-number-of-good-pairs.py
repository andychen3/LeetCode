class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash_map = {}
        ans = 0
        
        for num in nums:
            if num in hash_map:
                ans += hash_map[num]
            hash_map[num] = hash_map.get(num, 0) + 1
        return ans
            