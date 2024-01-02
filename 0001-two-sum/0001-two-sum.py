class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in hash_map:
                return [idx, hash_map[diff]]
            hash_map[num] = idx
        return [-1,-1]                