class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_set = collections.defaultdict(int)
        
        for index, val in enumerate(nums):
            diff = target-val
            if diff in hash_set:
                return [index, hash_set[diff]]
            hash_set[val] = index
        
        