
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        
        for index, num in enumerate(nums):
            ans = target-num
            if ans in hash_map:
                return [index, hash_map[ans]]
            hash_map[num] = index
        
        return -1